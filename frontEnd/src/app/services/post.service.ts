import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

const BASE_URL = 'https://jsonplaceholder.typicode.com/posts'

@Injectable({
  providedIn: 'root'
})
export class PostService {

private http = inject(HttpClient)
  constructor() { }

  getPosts(){
    return this.http.get(BASE_URL);
   }

}
