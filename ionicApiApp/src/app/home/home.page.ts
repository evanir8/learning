import { Component } from '@angular/core';
/*import { NavController } from 'ionic-angular';*/

//import { HeroService } from '../../providers/hero-service/hero-service';:

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})

export class HomePage {
  public obj: any;
  public heroes: any;

  constructor(public navCtrl: NavController, public heroService: HeroService) {
    this.getAllHeroes();
  }

  getAllHeroes() {
    this.heroService.load()
      .then(data => {
        this.obj = data;
        this.heroes = this.obj.data.results;
      });
  }

}
