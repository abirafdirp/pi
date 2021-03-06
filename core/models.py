from django.db import models
from django.contrib.auth.models import User


class Obat(models.Model):
    jenis = models.CharField(max_length=30)
    nama = models.CharField(max_length=30)
    harga = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Obat'

    def __str__(self):
        return self.nama


class Kunjungan(models.Model):
    tanggal = models.DateField()
    pasien = models.ForeignKey(User, related_name='kunjungan_pasien')
    biaya = models.IntegerField()
    obat = models.ManyToManyField(Obat)

    class Meta:
        verbose_name_plural = 'Kunjungan'

    def __str__(self):
        return str(self.tanggal) + ' ' + self.pasien.username


class AlatKB(models.Model):
    nama = models.CharField(max_length=30)
    periode_pemakaian = models.IntegerField(help_text='dalam hari')

    class Meta:
        verbose_name_plural = 'Alat KB'

    def __str__(self):
        return self.nama


class KB(models.Model):
    pasien = models.ForeignKey(User)
    alat_kb = models.ForeignKey(AlatKB)
    tanggal_mulai_pemakaian = models.DateField()
    tanggal_kontrol = models.DateField()

    class Meta:
        verbose_name_plural = 'KB'

    def __str__(self):
        return self.pasien.username + ' - ' + self.alat_kb.nama


TUJUAN_CHOICES = (
    ('konsultasi kehamilan', 'konsultasi kehamilan'),
    ('USG', 'USG'),
    ('melahirkan', 'melahirkan'),
    ('KB', 'KB'),
    ('imunisasi', 'imunisasi'),
    ('konsultasi ibu dan anak', 'konsultasi ibu dan anak')
)


class Pendaftaran(models.Model):
    pasien = models.ForeignKey(User)
    tanggal = models.DateField()
    tujuan_kunjungan = models.CharField(max_length=100, choices=TUJUAN_CHOICES)
    urutan_kunjungan = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Pendaftaran'

    def __str__(self):
        return '{} {} {}'.format(
            self.pasien.username,
            str(self.tanggal),
            self.tujuan_kunjungan
        )


JENIS_KELAMIN = (
    ('laki-laki', 'laki-laki'),
    ('perempuan', 'perempuan')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    nama = models.CharField(max_length=100, null=True, blank=True)
    jenis_kelamin = models.CharField(
        max_length=30, choices=JENIS_KELAMIN, null=True, blank=True
    )
    alamat = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=30, null=True, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)

