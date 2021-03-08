from django.contrib.auth.hashers import make_password
from django.db import models
import uuid
import time
import base64
import hmac



class UUIDTools(object):
    @staticmethod
    def uuid1_hex():
        return uuid.uuid1().hex


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=UUIDTools.uuid1_hex, editable=False)
    email = models.EmailField(max_length=100, unique=True, verbose_name='邮箱')
    password = models.CharField(max_length=256, verbose_name='密码')
    username = models.CharField(max_length=30, verbose_name='用户名', default='未设置')
    gender = models.BooleanField(verbose_name='性别', default=True)
    age = models.IntegerField(verbose_name='年龄', default=18)
    phone = models.CharField(max_length=100, verbose_name='电话', default='+86 999-999-999')
    activation = models.BooleanField(verbose_name='激活', default=False)
    isdelete = models.BooleanField(verbose_name='逻辑删除', default=False)

    class Meta:
        db_table = "User"

    # def save(self, *args, **kwargs):
    #     pbkdf2_sha256 = make_password(self.password.encode())
    #     self.password = pbkdf2_sha256
    #     super(User, self).save(*args, **kwargs)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.password = make_password(self.password)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)
    # def make_pwd(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.email


# class LoginTime(models.Model):
#     login_record = models.DateTimeField(auto_now_add=True)
#     login_UserAgent = models.CharField(max_length=256)
#     u_id = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     class Meta:
#         db_table = "LongTime"

def get_token(key, expire=180):
    '''
    :param key: str (用户给定的key，需要用s户保存以便之后验证token,每次产生token时的key 都可以是同一个key)
    :param expire: int(最大有效时间，单位为s)
    :return: token
    '''
    ts_str = str(time.time() + expire)
    ts_byte = ts_str.encode("utf-8")
    sha1_tshexstr  = hmac.new(key.encode("utf-8"),ts_byte,'sha1').hexdigest()
    token = ts_str+':'+sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
    return b64_token.decode("utf-8")


def out_token(key, token):
    '''
    :param key: 服务器给的固定key
    :param token: 前端传过来的token
    :return: true,false
    '''
    # token是前端传过来的token字符串
    try:
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            # token expired
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode("utf-8"),ts_str.encode('utf-8'),'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token certification failed
            return False
        # token certification success
        return True
    except Exception as e:
        print(e)


