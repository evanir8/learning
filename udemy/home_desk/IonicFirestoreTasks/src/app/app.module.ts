import { NgModule } from '@angular/core';
import { RouteReuseStrategy } from '@angular/router';

import { IonicModule, IonicRouteStrategy } from '@ionic/angular';
import { SplashScreen } from '@ionic-native/splash-screen/ngx';
import { StatusBar } from '@ionic-native/status-bar/ngx';

import { AppComponent } from './app.component';
import { AppRoutingModule } from './app-routing.module';
import { CoreModule } from 'src/app/core/core.module';

@NgModule({
  declarations: [AppComponent],
  imports: [CoreModule, AppRoutingModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
