<<<<<<< HEAD
# إعداد إرسال SMS باستخدام Twilio

## الخطوات:

### 1. تثبيت Twilio
```bash
pip install twilio
```

### 2. الحصول على حساب Twilio
1. اذهب إلى [Twilio.com](https://www.twilio.com) وسجل حساب مجاني
2. احصل على Account SID و Auth Token من لوحة التحكم
3. احصل على رقم Twilio لإرسال الرسائل منه

### 3. إضافة متغيرات البيئة

#### في Windows:
أنشئ ملف `.env` في مجلد المشروع وأضف:
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_FROM_NUMBER=+1234567890
```

أو قم بتعيين المتغيرات في PowerShell:
```powershell
$env:TWILIO_ACCOUNT_SID="your_account_sid_here"
$env:TWILIO_AUTH_TOKEN="your_auth_token_here"
$env:TWILIO_FROM_NUMBER="+1234567890"
```

### 4. التنشيط
بعد إضافة البيانات، سيتم إرسال الرسائل الفعلية بدلاً من وضع المحاكاة.

## ملاحظات:
- بدون بيانات Twilio، النظام يعمل في وضع المحاكاة ويطبع الرسائل في Console
- رسائل Twilio المجانية محدودة (ولكن كافية للاختبار)
- تأكد من تنسيق رقم الهاتف بشكل صحيح: +966XXXXXXXXX

=======
# إعداد إرسال SMS باستخدام Twilio

## الخطوات:

### 1. تثبيت Twilio
```bash
pip install twilio
```

### 2. الحصول على حساب Twilio
1. اذهب إلى [Twilio.com](https://www.twilio.com) وسجل حساب مجاني
2. احصل على Account SID و Auth Token من لوحة التحكم
3. احصل على رقم Twilio لإرسال الرسائل منه

### 3. إضافة متغيرات البيئة

#### في Windows:
أنشئ ملف `.env` في مجلد المشروع وأضف:
```
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_FROM_NUMBER=+1234567890
```

أو قم بتعيين المتغيرات في PowerShell:
```powershell
$env:TWILIO_ACCOUNT_SID="your_account_sid_here"
$env:TWILIO_AUTH_TOKEN="your_auth_token_here"
$env:TWILIO_FROM_NUMBER="+1234567890"
```

### 4. التنشيط
بعد إضافة البيانات، سيتم إرسال الرسائل الفعلية بدلاً من وضع المحاكاة.

## ملاحظات:
- بدون بيانات Twilio، النظام يعمل في وضع المحاكاة ويطبع الرسائل في Console
- رسائل Twilio المجانية محدودة (ولكن كافية للاختبار)
- تأكد من تنسيق رقم الهاتف بشكل صحيح: +966XXXXXXXXX

>>>>>>> ddcfc68 (first commit)
