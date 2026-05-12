import os
try:
    import yt_dlp
except ImportError:
    print("kütüphaneyi bulamadım")
    exit()

def sarki_indir(arama_terimi):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True,
        'extract_audio': True,
    }

    print(f"\n🔎 '{arama_terimi}' aranıyor ve indiriliyor")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            arama_sorgusu = f"ytsearch1:{arama_terimi}"
            
            info = ydl.extract_info(arama_sorgusu, download=False)
            if 'entries' in info and len(info['entries']) > 0:
                sarki_adi = info['entries'][0].get('title', 'Şarkıyı bulamadım')
                print(f"Bulundu: {sarki_adi}")
            
            ydl.download([arama_sorgusu])
            print("İndirme tamamlandı\n")
            
    except Exception as e:
        print(f"İndirilemedi. {e}\n")

def ana_menu():
    print("="*50)
    print("Müzik İndirici")
    print("="*50)
    
    klasor_adi = "Müzikler"
    if not os.path.exists(klasor_adi):
        os.makedirs(klasor_adi)
    
    os.chdir(klasor_adi)
    print(f"şarkılar şu klasöre inecek: {os.path.abspath('.')}\n")

    while True:
        istek = input("indirmek istediğiniz şarkıyı yazın: ").strip()
        
        if istek.lower() in ['exit']:
            print("kapatılıyor")
            break
            
        if istek:
            sarki_indir(istek)
        else:
            print("geçersiz şarkı adı")

if __name__ == "__main__":
    ana_menu()
