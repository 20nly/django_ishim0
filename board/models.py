from email.policy import default
from django.conf import settings
from django.db import models
from ishim import settings
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class CreateVacancy(models.Model):
# должность
    post = models.CharField(max_length=200, verbose_name='Должность')
# Сфера деятельности
    Field_of_activity = models.CharField(
        max_length = 50, choices=settings.FieldOfActivityList,
        null=True, blank=True, default=None, verbose_name='Сфера деятельности'
    )
# Какую зарплату вы предлагаете min и max
    salary_min = models.IntegerField(null=True, blank=True,verbose_name='Зарплата от')
    salary_max = models.IntegerField(null=True, blank=True,verbose_name='Зарплата до')   
# Прописка
    does_not_matter = models.BooleanField(verbose_name='не имеет значения')
    registration = models.CharField(
        max_length = 50, choices=settings.registrationList, 
        null=True, blank=True, default=None,verbose_name='Прописка'
    ) 

# TODO сделать кнопку не имеет значение, 
# которое при нажатии делает поле registration неактивной
    
# требования к сотруднику
    EmployeeRequirementsList=[
        (None,'не имеет значение'),
        (0,'нет опыта'),
        (3,'от 1-3 лет'),
        (5,'от 3-5 лет'),
        (6,'более 6 лет'),
    ]
    employee_requirements = models.IntegerField(
        choices=EmployeeRequirementsList, 
        null=True, blank=True, default=None,verbose_name='Требования к сотруднику'
    ) 
# возраст
    age_min = models.IntegerField(null=True, blank=True,verbose_name='Возраст от')
    age_max = models.IntegerField(null=True, blank=True,verbose_name='Возраст до')
# пол   
    sex = models.CharField(
        max_length = 50, choices=[
            ('male','мужской'),('female','женский'), (None, 'не имеет значения')
            ], 
        null=True, blank=True, default=None,verbose_name='Пол'
    )
# образование
    education = models.CharField(
        max_length = 50, choices=settings.educationList, 
        null=True, blank=True, default=None,verbose_name='Образование'
    )
# Владение языками
    # language = models.CharField(
    #     max_length = 50, choices=[
    #         ('eng','английский'),('rus','русский'), ('tur', 'туркменский')
    #         ], default='eng', verbose_name='Владение языками')
    # level = models.IntegerField(choices=[
    #         (0,'не владею'),(1,'элементарный'), (3, 'ниже среднего')
    #         ], default=0, null=True, blank=True,)

    # class Meta:
    #     verbose_name_plural = 'Дополнительные контакты'
    #     verbose_name = 'Дополнительный контакт'

# Обязанности
    responsibilities = models.TextField(
        max_length=200,null=True, blank=True, verbose_name='Обязанности'
        )
# Условия работы
    working_conditions = models.TextField(
        max_length=200,null=True, blank=True, verbose_name='Условия работы'
        )
    
# Занятость
    busyness = models.CharField(
        max_length = 50, 
        choices=[
            ('full','полная занятость'),('project_work','проектная работа'), 
            ('part_time', 'частичная занятость'), ('internship', 'стажировка')
            ], 
            default='full', verbose_name='Занятость', null=True, blank=True
            )
# График работы
    schedule = models.CharField(
        max_length = 50, 
        choices=[
            ('full','полная рабочий день'),('shift_schedule','сменный график'), 
            ('flexible_schedule', 'гибкий график'), ('remote_work', 'удаленная работа')
            ], 
            default='remote_work', verbose_name='График работы', null=True, blank=True
            )
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self):
        return self.post


class CreateResume(models.Model):
# Имя
    first_name = models.CharField(max_length=200, verbose_name='Имя')
# Фамилия
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
# Дата рождения  
    date_of_birth = models.DateField(
        null=True, blank=True, verbose_name='Дата рождения')
# Моб.телефон
    phone=PhoneNumberField(default=None,verbose_name='Моб.телефон')
# Эл.почта
    email = models.EmailField(max_length=500, blank=True, null=True, 
                                verbose_name='Эл.почта')
# Прописка
    does_not_matter = models.BooleanField(verbose_name='не имеет значения')
    registration = models.CharField(
        max_length = 50, choices=settings.registrationList, 
        null=True, blank=True, default=None,verbose_name='Прописка'
    )
# пол   
    sex = models.CharField(
        max_length = 50, choices=[
            ('male','мужской'),('female','женский')
            ], 
        null=True, blank=True, default=None,verbose_name='Пол'
    )
# должность
    post = models.CharField(max_length=200, verbose_name='Должность', null=True, blank=True)
    # TODO добавить список с должнастями 

# Сфера деятельности
    Field_of_activity = models.CharField(
        max_length = 50, choices=settings.FieldOfActivityList,
        null=True, blank=True, default=None, verbose_name='Сфера деятельности'
    )
# Зарплата
    salary_min = models.IntegerField(null=True, blank=True,verbose_name='Зарплата')
# Занятость
    busyness = models.CharField(
        max_length = 50, 
        choices=[
            ('full','полная занятость'),('project_work','проектная работа'), 
            ('part_time', 'частичная занятость'), ('internship', 'стажировка')
            ], 
            default='full', verbose_name='Занятость', null=True, blank=True
            )
# Опыт работы   
    work_experience = models.CharField(
        max_length = 50, choices=[
            ('yes','Есть опыт работы'),('no','Нет опыта работы')
            ], 
        null=True, blank=True, default='yes',verbose_name='Опыт работы '
    )
# должность
    past_post = models.CharField(max_length=200, verbose_name='Какую должность вы занимали?', null=True, blank=True)

# Как называлась организация ?
    firm_name = models.CharField(max_length=200, verbose_name='Как называлась организация?', null=True, blank=True)

# Обязательства
    responsibilities = models.TextField(
        max_length=200,null=True, blank=True, verbose_name='Обязательства'
        )
# Начало работы 
# TODO добавить https://django.fun/tutorials/kak-podklyuchit-vidzhet-vybora-daty-v-django/

# Окончание работы
# TODO добавить https://django.fun/tutorials/kak-podklyuchit-vidzhet-vybora-daty-v-django/

# Работаю по настоящее время
    steel_work = models.BooleanField(verbose_name='Работаю по настоящее время')

# TODO сделать кнопку добавить опыт работы,

# образование
    education = models.CharField(
        max_length = 50, choices=settings.educationList, 
        null=True, blank=True, default=None,verbose_name='Образование'
    )
# Учебное заведение
    universitet = models.CharField(max_length=200, verbose_name='Учебное заведение', null=True, blank=True)
# Факультет
    faculty = models.CharField(max_length=200, verbose_name='Факультет', null=True, blank=True)
# Специализация
    specialization = models.CharField(max_length=200, verbose_name='Специализация', null=True, blank=True)

# TODO сделать кнопку добавить образование
# TODO сделать кнопку добавить учебное заведение

# Знание программ  
    knowledge_of_programs = models.CharField(
        max_length = 50, choices=[
            ('1c','1C'),('ms_office','MS Office')
            ], 
        null=True, blank=True, default='ms_office',verbose_name='Знание программ '
    )
# Владение языками

# TODO добавить кнопку указать еще

# О себе
    about_yourself = models.TextField(
        max_length=200,null=True, blank=True, verbose_name='О себе'
        )
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    lang1 = models.ManyToManyField('Language', blank=True)
    
    


    def __str__(self):
        return self.firm_name
    

class Language(models.Model):
    language = models.CharField(
        max_length = 50, choices=[
            ('eng','английский'),('rus','русский'), ('tur', 'туркменский')
            ], default='eng', verbose_name='Владение языками')
    
    def __str__(self):
        return self.language

class LanguageLevel(models.Model):    
    level = models.IntegerField(choices=[
            (0,'не владею'),(1,'элементарный'), (3, 'ниже среднего')
            ], default=0, null=True, blank=True,)
    resume = models.ForeignKey(CreateResume, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.level