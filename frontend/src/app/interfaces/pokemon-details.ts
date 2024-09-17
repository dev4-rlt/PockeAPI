export type Ability = {
    ability: AbilityInfo;
}

export type AbilityInfo = {
    name: string;
    url: string;
    description: string;
}

export type AbilityDetails = {
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

export type PokemonDetail = {
    name: string;
    height: number;
    abilities: Ability[];
    base_experience: number;
    stats: Stat[];



    // forms: Form[]
    // game_indices: Index[]
    
    //held_items: HeldItem[]
    id: number
    is_default: boolean
    location_area_encounters: string
    // moves: Mfe[]
    
    order: number
    // species: Species
    // sprites: Sprites
    // stats: Stat[]
    // types: Type[]
    weight: number
  }