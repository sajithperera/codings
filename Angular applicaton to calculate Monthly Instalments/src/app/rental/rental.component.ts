import { Component, OnInit } from '@angular/core';
import {BankingService} from '../service/banking.service'

@Component({
  selector: 'app-rental',
  templateUrl: './rental.component.html',
  styleUrls: ['./rental.component.css']
})

export class RentalComponent implements OnInit {
  amount = 0;
  period = 0;
  rate = 0;
  rental_value = 0;

  constructor(
    private service: BankingService,
  ) { }

  CalculateRental() {
    const totalAmount = this.amount * (1 + this.rate/100);
    this.rental_value = totalAmount/this.period;
    
    this.service.UpdateRentalValue(this.rental_value);
    this.service.UpdateTotalamountValue(totalAmount);

    return this.rental_value.toFixed(3);
  }

  ngOnInit(): void {
  }

}
