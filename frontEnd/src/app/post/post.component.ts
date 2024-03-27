import { HttpClient } from '@angular/common/http';
import { Component, inject, OnInit } from '@angular/core';
import { PostService } from '../services/post.service';

@Component({
  selector: 'app-post',
  standalone: true,
  imports: [],
  templateUrl: './post.component.html',
  styleUrl: './post.component.css'
})
export class PostComponent implements OnInit {

  //http = inject(HttpClient);

  private postService = inject(PostService);

  posts : any = [];

  ngOnInit() : void{
        //this.fetchPosts();
        this.loadPosts();
  }

 /* fetchPosts(){
    this.http.get('https://jsonplaceholder.typicode.com/posts')
    .subscribe((posts: any)=>{
      console.log(posts);
      this.posts = posts;
    });

  }*/

  loadPosts(){
    this.postService.getPosts().subscribe((posts : any ) =>{
      console.log(posts);
      this.posts= posts;
    });
  }


}
