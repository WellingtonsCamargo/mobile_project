from selenium.webdriver.common.by import By

# Primeira tela
addPlanta = (By.ID, 'com.google.samples.apps.sunflower:id/add_plant')
toolBar = (By.ID, 'com.google.samples.apps.sunflower:id/toolbar')
plantList = (By.XPATH, '//android.widget.LinearLayout[@content-desc="Plant list"]/android.widget.TextView')
myGarden = (By.XPATH, '//android.widget.LinearLayout[@content-desc="My garden"]')
emptyGarden = (By.ID, 'com.google.samples.apps.sunflower:id/empty_garden')

# Segunda tela

listaPlantas = (By.ID, 'com.google.samples.apps.sunflower:id/plant_item_title')
filterZone = (By.ID, 'com.google.samples.apps.sunflower:id/filter_zone')


#app browser Google
appGoogle = (By.XPATH, '//android.widget.TextView[@content-desc="Chrome"]')
shearchBar = (By.ID, 'com.android.chrome:id/search_box_text')
icoB3 = (By.XPATH, '//android.support.v7.widget.RecyclerView[@content-desc="New tab"]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.view.View[2]')
textoB3 = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]')