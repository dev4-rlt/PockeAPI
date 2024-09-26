import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import { BaseUser, LoginUser } from '../interfaces/base-user';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  API: string = 'http://127.0.0.1:5000'

  constructor(private http: HttpClient) { }

  login(credentials: LoginUser): Observable<BaseUser> {
    return this.http.post<BaseUser>(`${this.API}/users/login`, credentials);
  }
}
