from django.db import models
import yfinance as yf
from decimal import Decimal
# Create your models here.
class portfolioItem(models.Model):
    symbol = models.CharField(max_length=10)
    boughtPrice = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.DecimalField(max_digits=10,decimal_places=6)

    def __str__(self):
        return self.symbol
    @property
    def name(self):
        try:
            ticker = yf.Ticker(self.symbol)
            return ticker.info.get("longName","Unknown")   
        except:
            return "Error"
    @property
    def currentPrice(self):
        try:
            ticker = yf.Ticker(self.symbol)
            return Decimal(str(ticker.info.get('regularMarketPrice', 0)))
        except:
            return Decimal("0.00")
    @property
    def profit(self):
        return self.currentPrice - self.boughtPrice
    @property
    def worth(self):
        return self.currentPrice * self.amount
    @property
    def profitPercentage(self):
     try:
        return (self.profit / self.boughtPrice) * 100
     except ZeroDivisionError:
        return 0