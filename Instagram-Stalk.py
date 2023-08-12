import instaloader
import tkinter as tk
from tkinter import messagebox
import instaloader
import tkinter as tk
from tkinter import messagebox

# Instaloader oturumunu yüklemek için kullanılacak değişkenler
instagram = instaloader.Instaloader()

def get_profile(username, password):
    try:
        instagram.load_session_from_file(username)  # Eğer oturum açılmışsa kullan
    except FileNotFoundError:
        instagram.context.log("Login required.")
        instagram.interactive_login(username)  # Oturum açma işlemi

    try:
        profile = instaloader.Profile.from_username(instagram.context, username)
        return profile
    except instaloader.ProfileNotExistsException:
        return None

def giris_yap():
    global username
    global password

    username = satır.get()
    password = satır2.get()

    profile = get_profile(username, password)

    if profile:
        messagebox.showinfo("Başarılı", "Giriş başarılı.")
    else:
        messagebox.showerror("Hata", "Giriş başarısız. Kullanıcı adı veya şifre yanlış.")

pencere = tk.Tk()
pencere.title("İnstagram")
pencere.geometry("200x250")
satır = tk.Entry(width=27)
satır.place(x=15, y=100)
satır2 = tk.Entry(width=27, show="*")
satır2.place(x=15, y=150)
giris = tk.Label(text="Giriş Ekranı")
giris.place(x=25, y=20)
giris.config(font=('Helvatical bold', 20))
girisok = tk.Button(text="Giriş Yap", font="Verdana 18 bold", command=giris_yap)
girisok.place(x=20, y=180)
isim = tk.Label(text="İSİM GİR")
isim.place(x=15, y=70)
sifre = tk.Label(text="ŞİFRE")
sifre.place(x=15, y=125)
pencere.mainloop()



def check_followers():

    try:
        instagram.load_session_from_file(username)
        if not instagram.context.is_logged_in:
            instagram.context.log("Session does not exist yet - Logging in.")
            instagram.interactive_login(username, password)

            # Oturumu kaydet
            instagram.save_session_to_file()

    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}")
        return

    target_account = entry_target_account.get()

    try:
        profil = instaloader.Profile.from_username(instagram.context, target_account)
        takipciler = profil.get_followers()

        search_user = entry_search_user.get()

        found = False

        for follower in takipciler:
            if search_user == follower.username:
                result_label.config(text=f"{search_user} kullanıcısı bulundu.")
                found = True
                break

        if not found:
            result_label.config(text=f"{search_user} kullanıcısı bulunamadı.")

    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}")

# Pencere oluşturma
root = tk.Tk()
root.title("Instagram Takipçi Kontrol Arayüzü")
# Hedef hesap giriş alanı
label_target_account = tk.Label(root, text="Hedef Hesap:")
label_target_account.pack()

entry_target_account = tk.Entry(root)
entry_target_account.pack()

# Aranacak kullanıcı adı giriş alanı
label_search_user = tk.Label(root, text="Aranacak Kullanıcı Adı:")
label_search_user.pack()

entry_search_user = tk.Entry(root)
entry_search_user.pack()

# Kontrol düğmesi
check_button = tk.Button(root, text="Kontrol Et", command=check_followers)
check_button.pack()

# Sonuç gösterme alanı
result_label = tk.Label(root, text="")
result_label.pack()

# GUI döngüsünü başlatma
root.mainloop()
def profil_foto_indir():
    profil_adi = resimkisi.get()
    if profil_adi:
        try:
            instagram = instaloader.Instaloader()
            instagram.download_profile(profile_name=profil_adi, profile_pic_only=True)
            bildirim.config(text=f"{profil_adi} profil resmi indirildi.")
        except Exception as e:
            bildirim.config(text=f"Hata: {str(e)}")

pencere = tk.Tk()
pencere.title("Instagram Profil Resmi İndirme")
pencere.geometry("400x200")

etiket = tk.Label(pencere, text="Kimin Profil Resmini İndirmek İstersiniz:")
etiket.pack(pady=10)

resimkisi = tk.Entry(pencere, width=30)
resimkisi.pack()

indir_button = tk.Button(pencere, text="İndir", command=profil_foto_indir)
indir_button.pack(pady=10)

bildirim = tk.Label(pencere, text="", fg="green")
bildirim.pack()

pencere.mainloop()

def get_followers():
    try:
        instagram.load_session_from_file(username)
        if not instagram.context.is_logged_in:
            instagram.context.log("Session does not exist yet - Logging in.")
            instagram.interactive_login(username, password)

            # Oturumu kaydet
            instagram.save_session_to_file()

    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}")
        return

    hesap = entry_target_username.get()

    try:
        profil = instaloader.Profile.from_username(instagram.context, hesap)
        takipciler = profil.get_followers()

        dosya_adi = f"{hesap}_takipciler.txt"

        with open(dosya_adi, "w", encoding="utf-8") as dosya:
            for takipci in takipciler:
                dosya.write(takipci.username + "\n")

        result_label.config(text=f"Tüm takipçiler '{dosya_adi}' dosyasına yazıldı.")

    except Exception as e:
        result_label.config(text=f"Hata: {str(e)}")

root = tk.Tk()
root.title("Instagram Takipçi Alma Arayüzü")
# Hedef kullanıcı adı giriş alanı
label_target_username = tk.Label(root, text="Hedef Kullanıcı Adı:")
label_target_username.pack()

entry_target_username = tk.Entry(root)
entry_target_username.pack()

# Takipçileri al düğmesi
get_followers_button = tk.Button(root, text="Takipçileri Al", command=get_followers)
get_followers_button.pack()

# Sonuç gösterme alanı
result_label = tk.Label(root, text="")
result_label.pack()

# GUI döngüsünü başlatma
root.mainloop()



