import { Routes } from '@angular/router';
import { PrincipalComponent } from './principal/principal.component';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NotFoundComponent } from './shared-components/not-found.component';
import { LoginGuard } from './login.guard';

export const routes: Routes = [
    { path: '', component: HomeComponent, canActivate: [LoginGuard] },
    { path: 'mostrador', component: PrincipalComponent, canActivate: [LoginGuard] },
    { path: 'login', component: LoginComponent },
    { path: 'dashboard', component: DashboardComponent, canActivate: [LoginGuard] },
    { path: '**', redirectTo: '' }
];
