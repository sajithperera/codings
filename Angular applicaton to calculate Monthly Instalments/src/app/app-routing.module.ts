import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {RentalComponent} from './rental/rental.component'
import {TableComponent} from './table/table.component'

const routes: Routes = [
  {path: '', component:RentalComponent},
  {path: 'table', component:TableComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
