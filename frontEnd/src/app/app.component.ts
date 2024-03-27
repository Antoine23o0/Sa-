import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { JoueurComponent } from './joueur/joueur.component';
import { PostComponent } from './post/post.component';
import { FormsModule } from '@angular/forms';

@Component({
    selector: 'app-root',
    standalone: true,
    templateUrl: './app.component.html',
    styleUrl: './app.component.css',
    imports: [RouterOutlet,JoueurComponent,PostComponent, FormsModule]
})
export class AppComponent {
  title = 'pingpong';
}
