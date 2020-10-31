import { Component, OnInit } from '@angular/core';
import { BankingService } from '../service/banking.service'

export class Data {
  public date;
  public paid: number;
  public due: number;
}

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})
export class TableComponent implements OnInit {

  dataSet: Data[] = [];
  TotalAmount: number;
  rental: number;

  constructor(
    private service: BankingService
  ) { }

  ngOnInit(): void {
    this.service.T_Amount.subscribe((res) => (this.TotalAmount = res));
    this.service.monthlyInstallment.subscribe((res) => (this.rental = res));

    this.AddDetails();
  }

  AddDetails() {

    var thisdate = new Date();
    thisdate.setMonth(thisdate.getMonth() - 1);

    let AmountPaid = this.rental;

    do{

      thisdate.setMonth(thisdate.getMonth() + 1);
      console.log(thisdate);

      let row = new Data();

      row.date = thisdate;
      row.paid = +AmountPaid.toFixed(3);
      row.due = +(this.TotalAmount - AmountPaid).toFixed(3);

      AmountPaid = AmountPaid + this.rental;

      this.dataSet.push(row);

    }while (AmountPaid <= this.TotalAmount && AmountPaid != 0) ;
  }

}
