export type BasePokemon = {
  codPokemon: number;
  name: string;
  attack: number;
  defense: number;
  height: number;
  weight: number;
  hp: number;
  specialAttack: number;
  specialDefense: number;
  speed: number;
};

export type PostPokemon = {
  name: string;
  height: number;
  weight: number;
  hp: number;
  attack: number;
  defense: number;
  specialAttack: number;
  specialDefense: number;
  speed: number;
  spriteFrontDefault: string;
  spriteFrontShiny: string;
};