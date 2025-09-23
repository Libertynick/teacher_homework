from frontend_tests_lesson.src.frontend.services.shop.elements.navbar_element.navbar_element import NavbarElement
from frontend_tests_lesson.src.frontend.services.shop.pages.catalog_page.models import Good
from frontend_tests_lesson.src.frontend.src.base_page.base_page import BasePage


class CatalogPageLocators:
    ITEM = '//div[@data-id="item-card"]'
    ADD_TO_CART_BTN = '//button[text()="Добавить в корзину"]'


class CatalogPage:

    def __init__(self, base_page: BasePage):
        self._base_page = base_page
        self.navbar_elem = NavbarElement(self._base_page)

    def open(self) -> 'CatalogPage':
        self.navbar_elem.open_catalog_page()
        return self

    def get_all_goods(self) -> list[Good]:
        goods_elems = self._base_page.get_all_elements(selector=CatalogPageLocators.ITEM)
        all_goods = []
        for i in range(len(goods_elems)):
            parsed_good = Good.from_string(text=goods_elems[i].text_content())
            parsed_good.index = i
            all_goods.append(parsed_good)
        return all_goods

    def add_good_to_cart(self, good: Good) -> None:
        all_bnt_elems = self._base_page.get_all_elements(selector=CatalogPageLocators.ADD_TO_CART_BTN)
        all_bnt_elems[good.index].click()
