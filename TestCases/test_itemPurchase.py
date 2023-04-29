import pytest
import softest
from Pages.protoCommercePage import protoComPage


@pytest.mark.usefixtures("setup")
class TestPurchaseItem(softest.TestCase):

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.protoPage = protoComPage(self.driver)

    def test_stepsToPurchase(self):
        #  Navigate to shop  # -------
        productPage = self.protoPage.navigateToShop()
        # Find product and add to cart  # -------
        productPage.scrollDown()
        productPage.enterProductName("iphone X")  # clicks checkout as well
        checkOutPage = productPage.checkout()
        # click on checkout button  # -------
        purchasePage = checkOutPage.checkout()  # clicks final checkout
        # select country  # -------
        purchasePage.selectCountry("Ind")  # selects "India"
        # complete purchase
        purchasePage.selectCheckbox()
        purchasePage.selectsSubmit()
        # validate completed purchase
        purchasePage.validatePurchaseMsg()
