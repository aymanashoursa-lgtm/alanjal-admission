# -*- coding: utf-8 -*-
"""
Script to fix all corrupted Arabic flash messages in app.py
"""
import re

# Complete list of all flash message fixes
# Format: (search_pattern, replacement, description)
ALL_FIXES = [
    # Login messages - admin_login
    (r'flash\("?\?[^"]*"\)\s*return redirect\(url_for\(\'admin_login\'\)\)', 
     'flash("لا يمكنك تسجيل الدخول كمدير من هنا")\n                return redirect(url_for(\'admin_login\'))',
     'Admin login - cannot login as director'),
    
    # Login error messages
    (r'flash\("?\?[^"]*"\)\s*return render_template\(\'admin_login\.html\'\)', 
     'flash("اسم المستخدم أو كلمة المرور غير صحيحة")\n    return render_template(\'admin_login.html\')',
     'Admin login - wrong credentials'),
    
    (r'flash\("?\?[^"]*"\)\s*return render_template\(\'director_login\.html\'\)', 
     'flash("اسم المستخدم أو كلمة المرور غير صحيحة")\n    return render_template(\'director_login.html\')',
     'Director login - wrong credentials'),
    
    (r'flash\("?\?[^"]*"\)\s*return render_template\(\'system_admin_login\.html\'\)', 
     'flash("اسم المستخدم أو كلمة المرور غير صحيحة")\n    return render_template(\'system_admin_login.html\')',
     'System admin login - wrong credentials'),
    
    # Director login permission
    (r'else:\s*flash\("?\?[^"]*"\)\s*#.*director', 
     'else:\n                flash("ليس لديك صلاحية الدخول كمدير")',
     'Director login - no permission'),
    
    # System admin login permission  
    (r'else:\s*flash\("?\?[^"]*"\)\s*#.*system_admin', 
     'else:\n                flash("ليس لديك صلاحية الدخول كمدير نظام")',
     'System admin login - no permission'),
    
    # User management
    (r'flash\("?\?[^"]*الاسم واسم المستخدم[^"]*"\)', 
     'flash("الاسم واسم المستخدم وكلمة المرور والنوع مطلوبون")',
     'Add user - required fields'),
    
    (r'flash\("?\?[^"]*اسم المستخدم موجود[^"]*"\)', 
     'flash("اسم المستخدم موجود بالفعل")',
     'Add user - username exists'),
    
    (r'flash\(f"\?[^"]*تم إضافة \{user_type_name\}[^"]*"\)', 
     'flash(f"تم إضافة {user_type_name} بنجاح")',
     'Add user - success'),
    
    (r'flash\("?\?[^"]*تم حذف المستخدم[^"]*"\)', 
     'flash("تم حذف المستخدم بنجاح")',
     'Delete user - success'),
    
    (r'flash\("?\?[^"]*النوع مطلوب"\)', 
     'flash("النوع مطلوب")',
     'Update user type - type required'),
    
    (r'flash\("?\?[^"]*تم تحديث نوع المستخدم[^"]*"\)', 
     'flash("تم تحديث نوع المستخدم بنجاح")',
     'Update user type - success'),
    
    # Student management
    (r'flash\("?\?[^"]*اسم المستخدم وكلمة المرور مطلوبان"\)', 
     'flash("اسم المستخدم وكلمة المرور مطلوبان")',
     'Add student - required fields'),
    
    (r'flash\(f"\?[^"]*تم إضافة طالب \{username\}[^"]*"\)', 
     'flash(f"تم إضافة طالب {username} بنجاح")',
     'Add student - success'),
    
    (r'flash\("?\?[^"]*تم حذف الطالب[^"]*"\)', 
     'flash("تم حذف الطالب بنجاح")',
     'Delete student - success'),
    
    (r'flash\("?\?[^"]*تم الموافقة على الطالب[^"]*"\)', 
     'flash("تم الموافقة على الطالب بنجاح")',
     'Approve student - success'),
    
    # Delete data
    (r'flash\("?\?[^"]*تم حذف جميع البيانات[^"]*"\)', 
     'flash("تم حذف جميع البيانات بنجاح")',
     'Delete all data - success'),
    
    (r'flash\("?\?[^"]*حدث خطأ أثناء حذف البيانات"\)', 
     'flash("حدث خطأ أثناء حذف البيانات")',
     'Delete all data - error'),
    
    (r'flash\("?\?[^"]*تم حذف جميع النتائج[^"]*"\)', 
     'flash("تم حذف جميع النتائج بنجاح")',
     'Delete all results - success'),
    
    # Add question
    (r'flash\("?\?[^"]*تم إضافة السؤال[^"]*\!\s*"\)', 
     'flash("تم إضافة السؤال بنجاح!")',
     'Add question - success'),
    
    (r'flash\(f"\?[^"]*حدث خطأ أثناء إضافة السؤال[^"]*"\)', 
     'flash(f"حدث خطأ أثناء إضافة السؤال: {str(e3)}")',
     'Add question - error'),
    
    # Export results
    (r"flash\('?\?[^']*يجب تسجيل الدخول[^']*'?\)", 
     "flash('يجب تسجيل الدخول أولاً')",
     'Export results - login required'),
    
    (r"flash\('?[^']*لا يوجد نتائج للتصدير'?\)", 
     "flash('لا يوجد نتائج للتصدير')",
     'Export results - no results'),
    
    # Generic fixes for patterns with just question marks and spaces
    (r'flash\("?\?\s{3}"\)', 'flash("تم حذف الطالب بنجاح")', 'Generic - 3 spaces'),
    (r'flash\("?\?\s{4}"\)', 'flash("ليس لديك صلاحية الدخول كمدير")', 'Generic - 4 spaces'),
    (r'flash\("?\?\s{5,}"\)', 'flash("ليس لديك صلاحية الدخول كمدير نظام")', 'Generic - 5+ spaces'),
]

def fix_file():
    """Read app.py, fix corrupted messages, and write back"""
    try:
        # Read with UTF-8 encoding
        with open('app.py', 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        original_content = content
        changes_made = 0
        
        # Apply all fixes
        for pattern, replacement, description in ALL_FIXES:
            new_content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            if new_content != content:
                print(f"✓ Fixed: {description}")
                content = new_content
                changes_made += 1
        
        # Write back if changes were made
        if content != original_content:
            with open('app.py', 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"\n✓ SUCCESS: Fixed {changes_made} flash message(s) in app.py")
            print("✓ File saved with UTF-8 encoding")
        else:
            print("⚠ No changes needed (patterns didn't match)")
            
    except Exception as e:
        print(f"✗ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    fix_file()
