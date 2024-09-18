import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatPokemonComponent } from './stat-pokemon.component';

describe('StatPokemonComponent', () => {
  let component: StatPokemonComponent;
  let fixture: ComponentFixture<StatPokemonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [StatPokemonComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(StatPokemonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
