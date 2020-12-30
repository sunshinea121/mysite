from django.db import models


class Idc(models.Model):
    """
    IDC表
    """
    name = models.CharField(max_length=10, unique=True, verbose_name="IDC名称")
    # person = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="联系人")
    phone = models.CharField(max_length=11, db_index=True, verbose_name="联系电话")
    address = models.CharField(max_length=30, verbose_name="地址")
    remark = models.CharField(max_length=100, blank=True, verbose_name="备注")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Cabinet(models.Model):
    """
    机柜模型
    """
    u_choices = (
        (1, "1U"),
        (2, "2U"),
        (3, "3U"),
        (4, "4U"),
        (5, "5U"),
        (6, "6U"),
        (7, "7U"),
        (8, "8U"),
        (9, "9U"),
        (10, "10U"),
        (11, "11U"),
        (12, "12U"),
        (13, "13U"),
        (14, "14U"),
        (15, "15U"),
        (16, "16U"),
        (17, "17U"),
        (18, "18U"),
        (19, "19U"),
        (20, "20U"),
        (21, "21U"),
        (22, "22U"),
        (23, "23U"),
        (24, "24U"),
    )
    name = models.CharField(max_length=10, unique=True, verbose_name="机柜名称")
    idc = models.ForeignKey(to="Idc", on_delete=models.CASCADE, verbose_name="所属IDC")
    u = models.ManyToManyField(to="CabinetU")

    def __str__(self):
        return str(self.name) + str(self.u)

    class Meta:
        # 联合唯一
        unique_together = (('name', 'u', 'idc'),)
        ordering = ('name',)


class CabinetU(models.Model):
    """
    机柜的U位
    """
    u_id = models.IntegerField()

    def __str__(self):
        return self.u_id

