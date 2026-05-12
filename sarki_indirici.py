import os
try:
    import yt_dlp
except ImportError:
    print("kütüphane bulunamadı.")
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

    print(f"\n🔎 '{arama_terimi}' aranıyor ve indiriliyor... Lütfen bekleyin.")
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            arama_sorgusu = f"ytsearch1:{arama_terimi}"
            
            info = ydl.extract_info(arama_sorgusu, download=False)
            if 'entries' in info and len(info['entries']) > 0:
                sarki_adi = info['entries'][0].get('title', 'Bilinmeyen Şarkı')
                print(f"🎵 Bulundu: {sarki_adi}")
            
            ydl.download([arama_sorgusu])
            print("İndirme başarıyla tamamlandı\n")
            
    except Exception as e:
        print(f"İndirilemedi. {e}\n")

def ana_menu():
    print("="*50)
    print("Müzik İndirici")
    print("="*50)
    print("Çıkmak için 'q' veya 'çıkış' yazın.\n")
    
    klasor_adi = "Müzikler"
    if not os.path.exists(klasor_adi):
        os.makedirs(klasor_adi)
    
    os.chdir(klasor_adi)
    print(f"Şarkılar şu klasöre indirilecek: {os.path.abspath('.')}\n")

    while True:
        istek = input("İndirmek istediğiniz şarkıyı yazın: ").strip()
        
        if istek.lower() in ['q', 'çıkış', 'cikis', 'quit', 'exit']:
            print("Programdan çıkılıyor.")
            break
            
        if istek:
            sarki_indir(istek)
        else:
            print("Lütfen geçerli bir şarkı adı yazın.")

if __name__ == "__main__":
    ana_menu()