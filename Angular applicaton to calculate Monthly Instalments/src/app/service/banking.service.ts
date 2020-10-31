import { Injectable } from '@angular/core';
import { BehaviorSubject } from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class BankingService {

  constructor() { }

  private installment = new BehaviorSubject(0);
  monthlyInstallment = this.installment.asObservable();
  
  private totalAmount = new BehaviorSubject(0);
  T_Amount = this.totalAmount.asObservable();

  UpdateRentalValue(newValue: number) {
    this.installment.next(newValue);
  }

  UpdateTotalamountValue(newTotal: number) {
    this.totalAmount.next(newTotal);
  }

}
