from selenium import webdriver
import time

def namefilm(film=''):
	# déclancher le driver
	if film.lower()[0:4] != "none":
		driver = webdriver.Chrome(executable_path="chromedriver.exe")
		driver.get("https://hdss-stream.org/")

		# recovers the search bar and add name of the film

		driver.find_element_by_id("s").send_keys(film)
		driver.find_element_by_css_selector("button.search-button").click()

		# recover the results

		time.sleep(2)

		results = driver.find_elements_by_css_selector("div.details")

		div = driver.find_elements_by_css_selector("div.title")
		date = driver.find_elements_by_css_selector("div.meta")
		contenant = driver.find_elements_by_css_selector("div.contenido")

		print(f"Film disponible pour la recherche : {film}\n")

		for i in div:
			title = i.find_element_by_css_selector("a")
			time.sleep(0.5)
			print(f'\nNom: {title.text}')
	else:
		driver = webdriver.Chrome(executable_path="chromedriver.exe")
		driver.get("https://hdss-stream.org/")
		print("Selection de la semaine : ")  # Afficher selection de la semaine
		featured_items_container = driver.find_element_by_css_selector("div.items.featured")
		featured_items = featured_items_container.find_elements_by_css_selector(".item.movies.smallWidthHomeItems")
		for featured_item in featured_items:
			data = featured_item.find_element_by_css_selector("div.data")
			balise_h3 = data.find_element_by_css_selector("h3")
			title = balise_h3.find_element_by_css_selector("a")
			print(f"\nNom du film : {title.text}",)



namefilm(input("Nom du film ( Ou 'none' pour voir la selection de la semaine ) > "))


