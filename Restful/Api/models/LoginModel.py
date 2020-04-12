from django.db import models


class LoginModel(models.Model):
    u_name = models.CharField(max_length=8)
    u_password = models.CharField(max_length=16)

    def to_dict(self):
        return {'id': self.id, 'u_name': self.u_name, 'u_password': self.u_password}
