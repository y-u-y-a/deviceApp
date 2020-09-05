from django.db import models


# get upload path
def load_path(instance, filename):
    path = '/'.join([str(instance.title) + str('.jpg')])
    return path


class Device(models.Model):

    class Meta:
        db_table = 'device' # device_deviceになってしまうため

    # blank: 入力必須, null: 空許可
    title = models.CharField(max_length=30, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to=load_path)

    # インスタンスにstrやprint関数を使うと__str__メソッドの戻り値が取得できる
    # このクラスのインスタンスの戻り値を指定
    def __str__(self):
        return self.title

