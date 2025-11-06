<<<<<<< HEAD
# دليل رفع نظام الاختبارات على سيرفر خارجي

## المتطلبات الأساسية

### 1. سيرفر (Server)
- **خيارات مجانية:**
  - PythonAnywhere (https://www.pythonanywhere.com) - سهل للمبتدئين
  - Heroku (https://www.heroku.com) - سهل ولكن بطيء في النسخة المجانية
  - Railway (https://railway.app) - مجاني لفترة محدودة
  - Render (https://render.com) - مجاني ولكن ينام بعد فترة من عدم الاستخدام
  - DigitalOcean (https://www.digitalocean.com) - يحتاج بطاقة ائتمان
  
- **خيارات مدفوعة (أفضل أداء):**
  - DigitalOcean Droplet
  - AWS EC2
  - Google Cloud Platform
  - Azure

### 2. متطلبات السيرفر
- Python 3.7 أو أحدث
- pip (مدير الحزم)
- git (لرفع الكود)

---

## خطوات الرفع (مثال على PythonAnywhere - الأسهل)

### المرحلة الأولى: التحضير

#### 1. تثبيت المتطلبات محلياً
```bash
pip install flask openpyxl pandas werkzeug
```

#### 2. اختبار النظام محلياً
```bash
python app.py
```
تأكد أن كل شيء يعمل على `http://127.0.0.1:5000`

#### 3. إنشاء ملف `.gitignore`
أنشئ ملف `.gitignore` في مجلد المشروع:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
env/
ENV/
.idea/
*.db
*.sqlite
*.sqlite3
exam.db
نتائج_الطلاب.xlsx
.env
```

### المرحلة الثانية: تعديل الكود للسيرفر

#### 1. تعديل إعدادات تشغيل Flask

في `app.py`، غيّر السطر الأخير (1279) من:
```python
app.run(debug=True)
```

إلى:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

#### 2. تأمين Secret Key
في `app.py`، السطر 10، غيّر:
```python
app.secret_key = "supersecretkey"
```
إلى:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY', 'supersecretkey-change-this-in-production')
```

---

## خيار 1: PythonAnywhere (الأسهل للمبتدئين)

### الخطوات:

#### 1. إنشاء حساب
اذهب إلى https://www.pythonanywhere.com وسجل حساب مجاني

#### 2. رفع الملفات
1. افتح **Files** من القائمة
2. اذهب إلى مجلد `home/username/`
3. أنشئ مجلد جديد: `myflaskapp`
4. ارفع الملفات التالية:
   - `app.py`
   - `requirements.txt`
   - مجلد `templates/` (كامل)
   - مجلد `static/` (كامل)

#### 3. تثبيت المكتبات
1. افتح **Consoles** ثم **Bash**
2. نفّذ الأوامر:
```bash
cd myflaskapp
pip3.10 install --user flask openpyxl pandas werkzeug twilio
```

#### 4. إعداد Web App
1. افتح **Web** من القائمة
2. اضغط **Add a new web app**
3. اختر **Flask** و Python version
4. اضغط **Next** ثم **Next**
5. في **Source code path** اكتب: `/home/username/myflaskapp`
6. في **Working directory** اكتب: `/home/username/myflaskapp`

#### 5. تعديل WSGI file
1. افتح ملف WSGI configuration
2. احذف كل شيء واستبدله بـ:
```python
import sys
path = '/home/username/myflaskapp'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

#### 6. تشغيل
1. أعد تحميل الصفحة (Reload)
2. افتح: `https://username.pythonanywhere.com`

---

## خيار 2: استخدام VPS (مثل DigitalOcean)

### الخطوات:

#### 1. إنشاء Droplet
1. سجل في DigitalOcean
2. اذهب إلى **Create** → **Droplets**
3. اختر:
   - **Ubuntu 22.04**
   - **Basic Plan** ($6/شهر)
   - **Datacenter** (اختر الأقرب لك)
4. اضغط **Create Droplet**

#### 2. الاتصال بالسيرفر
```bash
ssh root@your_server_ip
```

#### 3. إعداد السيرفر
```bash
# تحديث النظام
apt update && apt upgrade -y

# تثبيت Python و pip
apt install python3 python3-pip python3-venv git -y

# إنشاء مستخدم جديد
adduser myuser
usermod -aG sudo myuser
su - myuser
```

#### 4. رفع الكود
طريقة 1: Git
```bash
cd ~
git clone your_repository_url myflaskapp
cd myflaskapp
```

طريقة 2: SCP
من جهازك المحلي:
```bash
scp -r C:\Users\lenovo\Desktop\Flask_Exam_Project myuser@your_server_ip:~/myflaskapp
```

#### 5. إعداد البيئة الافتراضية
```bash
cd ~/myflaskapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 6. تثبيت Nginx و Gunicorn
```bash
# تثبيت Nginx
sudo apt install nginx -y

# تثبيت Gunicorn
pip install gunicorn
```

#### 7. إنشاء ملف Systemd Service
```bash
sudo nano /etc/systemd/system/myflaskapp.service
```

أضف:
```ini
[Unit]
Description=Gunicorn instance to serve myflaskapp
After=network.target

[Service]
User=myuser
Group=www-data
WorkingDirectory=/home/myuser/myflaskapp
Environment="PATH=/home/myuser/myflaskapp/venv/bin"
ExecStart=/home/myuser/myflaskapp/venv/bin/gunicorn --workers 3 --bind unix:myflaskapp.sock -m 007 app:app

[Install]
WantedBy=multi-user.target
```

#### 8. تشغيل الخدمة
```bash
sudo systemctl start myflaskapp
sudo systemctl enable myflaskapp
```

#### 9. إعداد Nginx
```bash
sudo nano /etc/nginx/sites-available/myflaskapp
```

أضف:
```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/myuser/myflaskapp/myflaskapp.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/myflaskapp /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### 10. إعداد Firewall
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## خيار 3: Render.com (مجاني)

### الخطوات:

#### 1. رفع الكود على GitHub
1. أنشئ حساب على GitHub
2. أنشئ repository جديد
3. ارفع كل الملفات:
```bash
git init
git add .
git commit -m "First commit"
git branch -M main
git remote add origin your_github_url
git push -u origin main
```

#### 2. الرفع على Render
1. سجل في https://render.com
2. اضغط **New** → **Web Service**
3. اربط repository الخاص بك
4. في الإعدادات:
   - **Name**: myflaskapp
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

#### 3. إضافة متغيرات البيئة
في **Environment**:
- `SECRET_KEY`: اختر مفتاح سري قوي
- `PORT`: 10000

#### 4. Deploy
اضغط **Create Web Service** وانتظر

---

## ملاحظات مهمة

### الأمان
1. **غير Secret Key** في الإنتاج
2. **استخدم HTTPS** (شهادات SSL من Let's Encrypt مجانية)
3. **قم بعمل نسخ احتياطي** من قاعدة البيانات
4. **حدّث النظام** بانتظام

### قاعدة البيانات
- **SQLite** مناسبة للتطوير
- **للإنتاج** فكّر في PostgreSQL أو MySQL للحجم الكبير

### متغيرات البيئة
لإضافة متغيرات سرية، استخدم ملف `.env`:
```bash
SECRET_KEY=your-super-secret-key-here
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
```

ثم في `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## استكشاف الأخطاء

### المشاكل الشائعة

**1. Error: Port already in use**
```bash
# في السيرفر، أوقف العملية
sudo lsof -i :5000
sudo kill -9 PID
```

**2. Error: Module not found**
```bash
# تأكد من تثبيت المكتبات
pip install -r requirements.txt
```

**3. Error: Permission denied**
```bash
# امنح الصلاحيات
sudo chmod -R 755 /path/to/app
```

---

## النسخ الاحتياطي

### قاعدة البيانات
```bash
# نسخ قاعدة البيانات
cp exam.db exam_backup.db

# أو إضافة نسخ احتياطي تلقائي
# استخدم cron job
0 2 * * * cp /path/to/exam.db /path/to/backup/exam_$(date +\%Y\%m\%d).db
```

---

## النطاق (Domain)

### ربط نطاق بالسيرفر
1. اذهب إلى provider النطاق
2. غيّر DNS records:
   - Type: A
   - Host: @
   - Value: your_server_ip

---

## المراقبة والصيانة

### مراقبة الأداء
```bash
# مراقبة الموارد
htop

# مراقبة الخدمات
sudo systemctl status myflaskapp

# مراقبة السجلات
tail -f /var/log/nginx/error.log
```

---

## الدعم

إذا واجهت مشاكل:
1. راجع السجلات (Logs)
2. تأكد من الإعدادات الصحيحة
3. تحقق من اتصال قاعدة البيانات
4. تأكد من صلاحيات الملفات

---

**نصيحة**: ابدأ بـ PythonAnywhere أو Render للممارسة، ثم انتقل لـ VPS عند الحاجة لأداء أفضل.

=======
# دليل رفع نظام الاختبارات على سيرفر خارجي

## المتطلبات الأساسية

### 1. سيرفر (Server)
- **خيارات مجانية:**
  - PythonAnywhere (https://www.pythonanywhere.com) - سهل للمبتدئين
  - Heroku (https://www.heroku.com) - سهل ولكن بطيء في النسخة المجانية
  - Railway (https://railway.app) - مجاني لفترة محدودة
  - Render (https://render.com) - مجاني ولكن ينام بعد فترة من عدم الاستخدام
  - DigitalOcean (https://www.digitalocean.com) - يحتاج بطاقة ائتمان
  
- **خيارات مدفوعة (أفضل أداء):**
  - DigitalOcean Droplet
  - AWS EC2
  - Google Cloud Platform
  - Azure

### 2. متطلبات السيرفر
- Python 3.7 أو أحدث
- pip (مدير الحزم)
- git (لرفع الكود)

---

## خطوات الرفع (مثال على PythonAnywhere - الأسهل)

### المرحلة الأولى: التحضير

#### 1. تثبيت المتطلبات محلياً
```bash
pip install flask openpyxl pandas werkzeug
```

#### 2. اختبار النظام محلياً
```bash
python app.py
```
تأكد أن كل شيء يعمل على `http://127.0.0.1:5000`

#### 3. إنشاء ملف `.gitignore`
أنشئ ملف `.gitignore` في مجلد المشروع:
```
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
venv/
env/
ENV/
.idea/
*.db
*.sqlite
*.sqlite3
exam.db
نتائج_الطلاب.xlsx
.env
```

### المرحلة الثانية: تعديل الكود للسيرفر

#### 1. تعديل إعدادات تشغيل Flask

في `app.py`، غيّر السطر الأخير (1279) من:
```python
app.run(debug=True)
```

إلى:
```python
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

#### 2. تأمين Secret Key
في `app.py`، السطر 10، غيّر:
```python
app.secret_key = "supersecretkey"
```
إلى:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY', 'supersecretkey-change-this-in-production')
```

---

## خيار 1: PythonAnywhere (الأسهل للمبتدئين)

### الخطوات:

#### 1. إنشاء حساب
اذهب إلى https://www.pythonanywhere.com وسجل حساب مجاني

#### 2. رفع الملفات
1. افتح **Files** من القائمة
2. اذهب إلى مجلد `home/username/`
3. أنشئ مجلد جديد: `myflaskapp`
4. ارفع الملفات التالية:
   - `app.py`
   - `requirements.txt`
   - مجلد `templates/` (كامل)
   - مجلد `static/` (كامل)

#### 3. تثبيت المكتبات
1. افتح **Consoles** ثم **Bash**
2. نفّذ الأوامر:
```bash
cd myflaskapp
pip3.10 install --user flask openpyxl pandas werkzeug twilio
```

#### 4. إعداد Web App
1. افتح **Web** من القائمة
2. اضغط **Add a new web app**
3. اختر **Flask** و Python version
4. اضغط **Next** ثم **Next**
5. في **Source code path** اكتب: `/home/username/myflaskapp`
6. في **Working directory** اكتب: `/home/username/myflaskapp`

#### 5. تعديل WSGI file
1. افتح ملف WSGI configuration
2. احذف كل شيء واستبدله بـ:
```python
import sys
path = '/home/username/myflaskapp'
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application
```

#### 6. تشغيل
1. أعد تحميل الصفحة (Reload)
2. افتح: `https://username.pythonanywhere.com`

---

## خيار 2: استخدام VPS (مثل DigitalOcean)

### الخطوات:

#### 1. إنشاء Droplet
1. سجل في DigitalOcean
2. اذهب إلى **Create** → **Droplets**
3. اختر:
   - **Ubuntu 22.04**
   - **Basic Plan** ($6/شهر)
   - **Datacenter** (اختر الأقرب لك)
4. اضغط **Create Droplet**

#### 2. الاتصال بالسيرفر
```bash
ssh root@your_server_ip
```

#### 3. إعداد السيرفر
```bash
# تحديث النظام
apt update && apt upgrade -y

# تثبيت Python و pip
apt install python3 python3-pip python3-venv git -y

# إنشاء مستخدم جديد
adduser myuser
usermod -aG sudo myuser
su - myuser
```

#### 4. رفع الكود
طريقة 1: Git
```bash
cd ~
git clone your_repository_url myflaskapp
cd myflaskapp
```

طريقة 2: SCP
من جهازك المحلي:
```bash
scp -r C:\Users\lenovo\Desktop\Flask_Exam_Project myuser@your_server_ip:~/myflaskapp
```

#### 5. إعداد البيئة الافتراضية
```bash
cd ~/myflaskapp
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### 6. تثبيت Nginx و Gunicorn
```bash
# تثبيت Nginx
sudo apt install nginx -y

# تثبيت Gunicorn
pip install gunicorn
```

#### 7. إنشاء ملف Systemd Service
```bash
sudo nano /etc/systemd/system/myflaskapp.service
```

أضف:
```ini
[Unit]
Description=Gunicorn instance to serve myflaskapp
After=network.target

[Service]
User=myuser
Group=www-data
WorkingDirectory=/home/myuser/myflaskapp
Environment="PATH=/home/myuser/myflaskapp/venv/bin"
ExecStart=/home/myuser/myflaskapp/venv/bin/gunicorn --workers 3 --bind unix:myflaskapp.sock -m 007 app:app

[Install]
WantedBy=multi-user.target
```

#### 8. تشغيل الخدمة
```bash
sudo systemctl start myflaskapp
sudo systemctl enable myflaskapp
```

#### 9. إعداد Nginx
```bash
sudo nano /etc/nginx/sites-available/myflaskapp
```

أضف:
```nginx
server {
    listen 80;
    server_name your_domain.com;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/myuser/myflaskapp/myflaskapp.sock;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/myflaskapp /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

#### 10. إعداد Firewall
```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## خيار 3: Render.com (مجاني)

### الخطوات:

#### 1. رفع الكود على GitHub
1. أنشئ حساب على GitHub
2. أنشئ repository جديد
3. ارفع كل الملفات:
```bash
git init
git add .
git commit -m "First commit"
git branch -M main
git remote add origin your_github_url
git push -u origin main
```

#### 2. الرفع على Render
1. سجل في https://render.com
2. اضغط **New** → **Web Service**
3. اربط repository الخاص بك
4. في الإعدادات:
   - **Name**: myflaskapp
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

#### 3. إضافة متغيرات البيئة
في **Environment**:
- `SECRET_KEY`: اختر مفتاح سري قوي
- `PORT`: 10000

#### 4. Deploy
اضغط **Create Web Service** وانتظر

---

## ملاحظات مهمة

### الأمان
1. **غير Secret Key** في الإنتاج
2. **استخدم HTTPS** (شهادات SSL من Let's Encrypt مجانية)
3. **قم بعمل نسخ احتياطي** من قاعدة البيانات
4. **حدّث النظام** بانتظام

### قاعدة البيانات
- **SQLite** مناسبة للتطوير
- **للإنتاج** فكّر في PostgreSQL أو MySQL للحجم الكبير

### متغيرات البيئة
لإضافة متغيرات سرية، استخدم ملف `.env`:
```bash
SECRET_KEY=your-super-secret-key-here
TWILIO_ACCOUNT_SID=your-twilio-sid
TWILIO_AUTH_TOKEN=your-twilio-token
```

ثم في `app.py`:
```python
from dotenv import load_dotenv
load_dotenv()
```

---

## استكشاف الأخطاء

### المشاكل الشائعة

**1. Error: Port already in use**
```bash
# في السيرفر، أوقف العملية
sudo lsof -i :5000
sudo kill -9 PID
```

**2. Error: Module not found**
```bash
# تأكد من تثبيت المكتبات
pip install -r requirements.txt
```

**3. Error: Permission denied**
```bash
# امنح الصلاحيات
sudo chmod -R 755 /path/to/app
```

---

## النسخ الاحتياطي

### قاعدة البيانات
```bash
# نسخ قاعدة البيانات
cp exam.db exam_backup.db

# أو إضافة نسخ احتياطي تلقائي
# استخدم cron job
0 2 * * * cp /path/to/exam.db /path/to/backup/exam_$(date +\%Y\%m\%d).db
```

---

## النطاق (Domain)

### ربط نطاق بالسيرفر
1. اذهب إلى provider النطاق
2. غيّر DNS records:
   - Type: A
   - Host: @
   - Value: your_server_ip

---

## المراقبة والصيانة

### مراقبة الأداء
```bash
# مراقبة الموارد
htop

# مراقبة الخدمات
sudo systemctl status myflaskapp

# مراقبة السجلات
tail -f /var/log/nginx/error.log
```

---

## الدعم

إذا واجهت مشاكل:
1. راجع السجلات (Logs)
2. تأكد من الإعدادات الصحيحة
3. تحقق من اتصال قاعدة البيانات
4. تأكد من صلاحيات الملفات

---

**نصيحة**: ابدأ بـ PythonAnywhere أو Render للممارسة، ثم انتقل لـ VPS عند الحاجة لأداء أفضل.

>>>>>>> ddcfc68 (first commit)
