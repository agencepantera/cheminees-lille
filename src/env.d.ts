/// <reference types="astro/client" />

// Déclaration de type pour AOS
declare const AOS: {
  init: (options?: {
    duration?: number;
    once?: boolean;
    // Ajoutez d'autres options selon vos besoins
  }) => void;
};