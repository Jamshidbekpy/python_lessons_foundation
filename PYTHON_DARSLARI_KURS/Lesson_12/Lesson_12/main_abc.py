from abc import ABC, abstractmethod
from datetime import datetime
class ShopStructure(ABC):
    # Adds a new product to the shop.
    #
    # @return None
    @abstractmethod
    def add(self)->None:
        """
        Adds a new product to the shop.

        :return: None
        """
        pass
    # Sells a product from the shop.
    #
    # @return: None
    @abstractmethod
    def sell(self)->None:
        """
        Sells a product from the shop.

        :return: None
        """
        pass
    # Reports the shop's current state.
    #
    # @return: None
    @abstractmethod
    def report(self)->None:
        """
        Reports the shop's current state.

        This method is used to display the current state of the shop,
        such as the number of products, total price, etc.

        :return: None
        """
        pass
    # The main method of the ProductStructure class.
    #
    # This method is the entry point for a product in the shop.
    #
    # When this method is called, the product is expected to perform
    # some action, such as selling itself, or reporting its state.
    #
    # This method should not return anything, since it is expected to
    # have a side effect on the shop or the product itself.
    #
    # :return: None
    @abstractmethod
    def main(self)->None:
        """
        The entry point for a product in the shop.

        This method is called when the product is added to the shop,
        or when the shop wants to interact with the product in some way.

        The method is expected to have a side effect on the shop or the
        product itself, such as selling the product, or reporting its
        state.

        This method should not return anything.

        :return: None
        """
        pass

    
class ProductStructure(ABC):

    @abstractmethod
    def get_quantity(self)->int:
        """
        Returns the quantity of the product.

        The quantity is the number of units of the product available in the
        shop.

        :return: The quantity of the product
        :rtype: int
        """
        pass
    @abstractmethod
    def get_price(self)->float:
        """
        Returns the price of the product.

        The price is the amount that the customer will pay for the product.

        :return: The price of the product
        :rtype: float
        """
        pass
    @abstractmethod
    def get_old_date(self)->datetime:
        """
        Returns the date the product was added to the shop.

        This is useful for calculating how long a product has been in the
        shop, or for sorting products by their age.

        :return: The date the product was added to the shop
        :rtype: datetime
        """
        pass
    @abstractmethod
    def get_expiration_date(self)->datetime:
        """
        Returns the date the product is expected to expire.

        This method is used to calculate how long a product has before it
        expires, or to determine if a product has expired.

        :return: The date the product is expected to expire
        :rtype: datetime
        """
        pass
    def get_date_of_arrival(self)->datetime:
        """
        Returns the date the product was received by the shop.

        This is useful for sorting products by their arrival date.

        :return: The date the product was received by the shop
        :rtype: datetime
        """
        pass


            
            
            
    