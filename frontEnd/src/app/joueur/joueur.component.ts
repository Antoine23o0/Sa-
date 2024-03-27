import { NgFor } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component, inject, OnInit } from '@angular/core';
import { FormsModule} from '@angular/forms';
import { JoueurService } from '../services/joueur.service';

@Component({
  selector: 'app-joueur',
  standalone: true,
  imports : [NgFor, FormsModule],
  templateUrl: './joueur.component.html',
  styleUrls: ['./joueur.component.css']
})

export class JoueurComponent implements OnInit {

  joueurs : any = [];

  private joueurSer = inject(JoueurService);

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    //this.fetchPosts();
    this.loadPosts();
  }

  ajouterJoueur(data : any){
    console.warn(data)

    this.joueurSer.ajouterJoeur(data).subscribe((response)=>{
      console.warn(response)
    });
  }

  loadPosts() {
        this.joueurSer.getJoueurs().subscribe((joueurs : any ) => {
                console.log(joueurs);
                this.joueurs = joueurs;
        });
  }



/*  ajouterJoueur() {
    this.joueurSer.ajouterJoueur(this.nom, this.age,this.prenom).subscribe((response) => {
        console.log('Joueur ajouté avec succès', response);
        this.nom = '';
        this.age = 0;
        this.prenom = '';
      },
      (error) => {
        console.error('Erreur lors de l\'ajout du joueur', error);
      }
    );
  }*/

  /*ajouterJoueur(data : any)
  {
    console.warn(data)
  }*/


}
