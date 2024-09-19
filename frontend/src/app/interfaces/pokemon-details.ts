export type Ability = {
    ability: AbilityInfo;
}

export type AbilityInfo = {
    name: string;
    url: string;
    description: string;
}

export type EffectDetails = {
    flavor_text_entries: FlavorTextEntry[];
}

export type FlavorTextEntry = {
    flavor_text: string;
    language: Language;
}

export type Language = {
    name: string;
}

export type Stat = {
    base_stat: number;
    stat: StatDescription;
}

export type StatDescription = {
    name: string;
}

export type MoveInfo = {
    move: Move;
}

export type Move = {
    name: string;
    url: string;
    description: string;
}

export type Index = {
    game_index: number;
    version: Version;
}

export type Version = {
    name: string;
}

export type Sprites = {
    front_default: string
    front_shiny: string
}

export type Location = {
    location_area: LocationName;
}

export type LocationName = {
    name: string;
    url: string;
}

export type LocationInfo = {
    location: LocationName;
}

export type PokemonDetail = {
    id: number
    name: string;
    height: number;
    weight: number;
    abilities: Ability[];
    base_experience: number;
    stats: Stat[];
    moves: MoveInfo[];
    game_indices: Index[];
    location_area_encounters: string;
    locations: LocationInfo[];
    sprites: Sprites;

    //held_items: HeldItem[]
    // species: Species
    // stats: Stat[]
    // types: Type[]
    
  }