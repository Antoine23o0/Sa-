import { HttpClient } from '@angular/common/http';
import { inject, Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class JoueurService {

  private http =inject(HttpClient)

  constructor() {}

  getJoueurs(){
    return this.http.get('http://127.0.0.1:5000/joueurs');
  }

  ajouterJoeur(nouveauJoueur: any){
    return this.http.post('http://127.0.0.1:5000/joueurs/ajouter_joueur',nouveauJoueur)
  }




 /* ajouterJoueur(nom: string, age: number, prenom : string) {
    const nouveauJoueur = {
      nom: nom,
      prenom : prenom,
      age: age
    };

    // Envoi de la requête POST pour ajouter le joueur
    return this.http.post('http://127.0.0.1:5000/joueurs/ajouter_joueur', nouveauJoueur);
  }*/




}
