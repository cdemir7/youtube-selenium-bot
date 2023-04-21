# Driver import edilir
from selenium import webdriver 
# Butona tıklama işlemi için Keys import edilir
from selenium.webdriver.common.keys import Keys
# Xpath'i kullanmak için import edilir
from selenium.webdriver.common.by import By
# İşlemler arasında duraklamalar yapılmak için import edilir
import time

# Class yapısı oluşturuldu
class Youtube:
    def __init__(self):
        self.browser = webdriver.Chrome() # Her açılışta çalışması için webdriver init metodunda oluşturuldu.
        

    def kesfet(self):
        self.browser.get("https://www.youtube.com/") # Verilen Url'e gidildi.
        self.browser.maximize_window() # Chrome penceresi tam ekran yapıldı.
        time.sleep(3)
        # Trendler butonunun yolu belirtildi.
        trendler = self.browser.find_element(by = By.XPATH, value='/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[3]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item/yt-formatted-string')
        # Trendler butonuna tıklandı.
        trendler.click()
        time.sleep(3)

        trend_video = []

        liste = self.browser.find_elements(by = By.XPATH, value='//*[@id="video-title"]/yt-formatted-string')
        time.sleep(2)
        #print("count: " + str(len(liste)))

        
        for i in liste:
            trend_video.append(i.text)

        # Burada scroll un maksimum değeri alındı
        scroll_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            # Aşağıda scrollun gidebileceği yere kadar gidip sayfaya başka videolar yüklenince de daha aşağı gitmesi sağlandı.
            self.browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            if scroll_height == new_height:
                break

            scroll_height = new_height

            for i in liste:
                trend_video.append(i.text)

        liste = self.browser.find_elements(by = By.XPATH, value='//*[@id="video-title"]/yt-formatted-string')
        time.sleep(2)
        print("Toplam Video Sayısı: " + str(len(liste)))

        # Aşağıda trend_video dizisindeki stringler txt uzantılı dosyaya yazıldı.
        count = 1
        with open('Trend-Videolar.txt', 'w', encoding='UTF-8') as file:
            for item in trend_video:
                file.write(f"{count}-{item}\n")
                count += 1

        
ytb = Youtube()
ytb.kesfet()