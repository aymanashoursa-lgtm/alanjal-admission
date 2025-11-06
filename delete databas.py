<<<<<<< HEAD
import sqlite3
import os


# تأكد من إيقاف تطبيق Flask أولاً
def delete_all_data():
    try:
        conn = sqlite3.connect("exam.db")
        cursor = conn.cursor()

        # امسح جميع الجداول
        cursor.execute("DELETE FROM results")
        cursor.execute("DELETE FROM questions")
        cursor.execute("DELETE FROM students")

        # إعادة تعيين الأرقام التلقائية
        cursor.execute("DELETE FROM sqlite_sequence")

        conn.commit()

        # تحقق من المسح
        cursor.execute("SELECT COUNT(*) FROM results")
        remaining_results = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM questions")
        remaining_questions = cursor.fetchone()[0]

        conn.close()

        print(f"✅ تم المسح - السجلات المتبقية: {remaining_results} نتيجة, {remaining_questions} سؤال")

        if remaining_results > 0 or remaining_questions > 0:
            print("⚠️ لا يزال هناك سجلات! جرب الحل 2")

    except Exception as e:
        print(f"❌ خطأ: {e}")


=======
import sqlite3
import os


# تأكد من إيقاف تطبيق Flask أولاً
def delete_all_data():
    try:
        conn = sqlite3.connect("exam.db")
        cursor = conn.cursor()

        # امسح جميع الجداول
        cursor.execute("DELETE FROM results")
        cursor.execute("DELETE FROM questions")
        cursor.execute("DELETE FROM students")

        # إعادة تعيين الأرقام التلقائية
        cursor.execute("DELETE FROM sqlite_sequence")

        conn.commit()

        # تحقق من المسح
        cursor.execute("SELECT COUNT(*) FROM results")
        remaining_results = cursor.fetchone()[0]

        cursor.execute("SELECT COUNT(*) FROM questions")
        remaining_questions = cursor.fetchone()[0]

        conn.close()

        print(f"✅ تم المسح - السجلات المتبقية: {remaining_results} نتيجة, {remaining_questions} سؤال")

        if remaining_results > 0 or remaining_questions > 0:
            print("⚠️ لا يزال هناك سجلات! جرب الحل 2")

    except Exception as e:
        print(f"❌ خطأ: {e}")


>>>>>>> ddcfc68 (first commit)
delete_all_data()