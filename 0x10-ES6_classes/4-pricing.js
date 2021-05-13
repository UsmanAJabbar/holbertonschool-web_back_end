// Class Pricing
import Currency from './3-currency';

export default class Pricing {
  constructor(amount, currency) {
    this.amount = amount;
    this.currency = currency;
  }

  get amount() { return this._amount; }

  set amount(newAmount) {
    if (typeof newAmount !== 'number') { throw TypeError('Amount must be a number'); }
    this._amount = newAmount;
  }

  get currency() { return this._currency; }

  set currency(newCurrency) {
    if (!(newCurrency instanceof Currency)) { throw TypeError('Currency must be an instance of Currency'); }
    this._currency = newCurrency;
  }

  displayFullPrice() {
    return `${this.amount} ${this.currency.name} (${this.currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    if (typeof amount !== 'number' || typeof conversionRate !== 'number') {
      throw TypeError('Amount / Conversion Rate must be numbers');
    }
    return amount * conversionRate;
  }
}
