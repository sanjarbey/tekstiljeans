from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class WeightMaterial(models.Model):
    """Материалнинг оғирлиги"""
    material = models.CharField(verbose_name="Материал", max_length=250)
    weight = models.CharField(verbose_name="Оғирлиги", max_length=250)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} ".format(self.material, self.weight)

    class Meta:
        verbose_name = "Материалнинг оғирлиги "
        verbose_name_plural = "Материалларнинг оғирлиги "

class TypeMaterial(models.Model):
    """Материалнинг тўқилиш тури"""
    name = models.CharField(verbose_name="Материал", max_length=250)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} ".format(self.name)

    class Meta:
        verbose_name = "Материалнинг тўқилиш тури"
        verbose_name_plural = "Материалларнинг тўқилиш тури"


class ContentMaterial(models.Model):
    """Материалнинг толавий таркиби"""
    name = models.CharField(verbose_name="Материалнинг толавий таркиби", max_length=250)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} ".format(self.name)

    class Meta:
        verbose_name = "Материалнинг толавий таркиби "
        verbose_name_plural = "Материалнинг толавий таркиби"

class ColorsMaterial(models.Model):
    """Материалнинг ранглари"""
    name = models.CharField(verbose_name="Материалнинг ранги номи ", max_length=250)
    photo = models.ImageField(verbose_name="Изображение", upload_to="jeanscolor/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} ".format(self.name)

    class Meta:
        verbose_name = "Материалнинг ранги "
        verbose_name_plural = "Материалларнинг ранглари "

class ChemicalName(models.Model):
    """Химикатлар номи, тури"""
    name = models.CharField(verbose_name="Химикат номи	", max_length=250)
    chemicalformul = models.CharField(verbose_name="Кимевий формуласи", max_length=250, default=None, blank=True,)
    view = models.ImageField(verbose_name="Расм	", upload_to="chemicalcolors/")
    varki = models.DecimalField(verbose_name="Количество для типа варки, гр",null=True, blank=True, max_digits=11, decimal_places=2,
                               validators=[MinValueValidator(Decimal('0.00'))])
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {}".format(self.name,  self.varki)

    class Meta:
        verbose_name = "Химикат номи, тури "
        verbose_name_plural = "Химикатлар номлари, турлари "

class CountryName(models.Model):
    """Название страны"""
    name = models.CharField(verbose_name="Название страна", max_length=250,blank=True)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} ".format(self.name)

    class Meta:
        verbose_name = "Название страна "
        verbose_name_plural = "Название страны"

class SewingThreads(models.Model):
    """
    Швейные нитки
    Ички чокларни тикиш учун иплар намунаси
    """
    country = models.ForeignKey(CountryName,verbose_name="Название страна", on_delete=models.SET_NULL, blank=True, null=True)
    gradethread = models.CharField(verbose_name="Название сорт  (100% РЕ)", max_length=250, default=None,null=True, blank=True,)
    modelthread = models.CharField(verbose_name="Название модель", max_length=250, default=None,null=True, blank=True,)
    photo = models.ImageField(verbose_name="Вид	", upload_to="threadphoto/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} ".format(self.gradethread,self.modelthread, self.country)

    class Meta:
        verbose_name = "Ички чокни тикиш учун ип намунаси "
        verbose_name_plural = "Ички чокларни тикиш учун иплар намунаси"

class DecorativeThreads(models.Model):
    """
    Схема ниток для выполнения декоративных строчек
    Безак чокларни тикиш учун иплар намунаси
    """
    country = models.ForeignKey(CountryName,verbose_name="Название страна", on_delete=models.CASCADE,blank=True)
    gradethread = models.CharField(verbose_name="Название сорт  (100% РЕ)", max_length=250, default=None, null=True,blank=True, )
    modelthread = models.CharField(verbose_name="Название модель", max_length=250, default=None,null=True, blank=True,)
    photo = models.ImageField(verbose_name="Вид	", upload_to="decorphoto/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} ".format(self.gradethread, self.modelthread, self.country)

    class Meta:
        verbose_name = "Безак чокни тикиш учун ип намунаси"
        verbose_name_plural = "Безак чокларни тикиш учун иплар намунаси"

class DlinaMolniy(models.Model):
    """Молния Длина"""
    name = models.CharField(verbose_name="Длина Молния", max_length=250)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {}  ".format(self.name)

    class Meta:
        verbose_name = "Молния Длина "
        verbose_name_plural = "Молния Длина "

class Molniya(models.Model):
    """
    Молния тақилма
    """
    modelmolniy = models.CharField(verbose_name="Название модель", max_length=250, default=None,null=True, blank=True,)
    molniydilin = models.ForeignKey(DlinaMolniy,verbose_name="Длина Молния ", on_delete=models.SET_NULL,blank=True, null=True)
    colormolniy = models.CharField(verbose_name="Название Цвет", max_length=250, default=None, null=True,blank=True, )
    zvena = models.CharField(verbose_name="Название Материал звена", max_length=250, default=None, null=True,blank=True, )
    colorzvena = models.CharField(verbose_name="Название Цвет звена", max_length=250, default=None, null=True,blank=True, )
    photo = models.ImageField(verbose_name="Молния	", upload_to="molniyphoto/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} => {} => {} ".format(self.modelmolniy,self.molniydilin, self.colormolniy)

    class Meta:
        verbose_name = "Молния  тип "
        verbose_name_plural = "Молния  тип "


class Knopok(models.Model):
    """
    Типы кнопок
    Тугма турлари
    """
    modelknopok = models.CharField(verbose_name="Название модель", max_length=250, default=None,null=True, blank=True,)
    materialknopok = models.CharField(verbose_name="Материал)", max_length=250, default=None, null=True, blank=True, )
    diametrknopok = models.DecimalField(verbose_name="Диаметр  ",null=True, blank=True, max_digits=11, decimal_places=2,
                 validators=[MinValueValidator(Decimal('0.00'))])
    colorknopok = models.CharField(verbose_name="Название Цвет", max_length=250, default=None, null=True,blank=True, )
    photo = models.ImageField(verbose_name="Пуговицы	", upload_to="knopokphoto/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} ".format(self.modelknopok, self.materialknopok)

    class Meta:
        verbose_name = "Kнопок  тип "
        verbose_name_plural = "Kнопок  тип "

class Zaklepka(models.Model):
    """
    Типы Заклепка
    Заклепка турлари
    """
    materialzaklepka = models.CharField(verbose_name="Материал)", max_length=250, default=None, null=True, blank=True, )
    diametrzaklepka = models.DecimalField(verbose_name="Диаметр  ",null=True, blank=True, max_digits=11, decimal_places=2,
                 validators=[MinValueValidator(Decimal('0.00'))])
    colorzaklepka = models.CharField(verbose_name="Название Цвет", max_length=250, default=None, null=True,blank=True, )
    photo = models.ImageField(verbose_name="Заклепки	", upload_to="zaklepkaphoto/")
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} => {}".format(self.materialzaklepka, self.diametrzaklepka,self.colorzaklepka)

    class Meta:
        verbose_name = "Заклепка  тип "
        verbose_name_plural = "Заклепка  тип "

class Costumer(models.Model):
    """
    Mijoz haqida
    """
    name = models.CharField(verbose_name="F.I.O", max_length=250)
    organization= models.CharField(verbose_name="Tashkiloti", max_length=250)
    phone= models.CharField(verbose_name="Telefon nomer", max_length=250)
    email= models.CharField(verbose_name="Elektron pochta", max_length=250)
    adrres= models.CharField(verbose_name="Manzili", max_length=250)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " {} => {} => {}".format(self.name, self.organization, self.phone,self.email)

    class Meta:
        verbose_name = "Мижоз "
        verbose_name_plural = "Мижозлар "

class CostumerRecommen(models.Model):
    """
    Mijozga tavsiya etiladigan jeansni yig'ish
    """
    costumer = models.ForeignKey(Costumer,verbose_name="Mijoz", on_delete=models.SET_NULL, blank=True, null=True)
    serial_number = models.IntegerField(verbose_name="Buyurtma raqami ",  unique=True, blank=True, null=True)
    weightmaterial = models.ForeignKey(WeightMaterial,verbose_name="Материалнинг оғирлиги", on_delete=models.SET_NULL, blank=True, null=True)
    typematerial = models.ForeignKey(TypeMaterial,verbose_name="Материалнинг тўқилиш туриz", on_delete=models.SET_NULL, blank=True, null=True)
    contentmaterial = models.ForeignKey(ContentMaterial,verbose_name="Материалнинг толавий таркиби", on_delete=models.SET_NULL, blank=True, null=True)
    colorsmaterial = models.ForeignKey(ColorsMaterial,verbose_name="Материалнинг ранги", on_delete=models.SET_NULL, blank=True, null=True)
    chemicalname = models.ManyToManyField(ChemicalName,verbose_name="Химикатлар номи, тури")
    sewingthreads = models.ForeignKey(SewingThreads,verbose_name="Ички чокларни тикиш учун иплар намунаси", on_delete=models.SET_NULL, blank=True, null=True)
    decorativethreads = models.ForeignKey(DecorativeThreads,verbose_name="Безак чокларни тикиш учун иплар намунаси", on_delete=models.SET_NULL, blank=True, null=True)
    molniya = models.ForeignKey(Molniya,verbose_name="Молния тақилма", on_delete=models.SET_NULL, blank=True, null=True)
    knopok = models.ForeignKey(Knopok,verbose_name="Тугма турлари", on_delete=models.SET_NULL, blank=True, null=True)
    zaklepka = models.ForeignKey(Zaklepka,verbose_name="Заклепка турлари", on_delete=models.SET_NULL, blank=True, null=True)
    url = models.SlugField(max_length=260, unique=True)
    status = models.BooleanField(default=True, verbose_name='Статус')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return " {} => {} ".format(self.costumer,self.serial_number)

    class Meta:
        verbose_name = "Мижозга тавсия "
        verbose_name_plural = "Мижозларга тавсиялар "



