import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  exports: [ CommonModule, ReactiveFormsModule, IonicModule ]
})
export class SharedModule { }
