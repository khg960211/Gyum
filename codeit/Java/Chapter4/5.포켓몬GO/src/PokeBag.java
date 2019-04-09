import java.util.ArrayList;
import java.util.HashMap;

public class PokeBag {
    private final HashMap<String, ArrayList<Pokemon>> pokemons = new HashMap<>();

    public ArrayList<Pokemon> getPokemons(String name) {
        return pokemons.get(name);
    }

    public void add(Pokemon pokemon) {
        String name = pokemon.name;

        // 새로운 포켓몬이라면 포켓몬 이름과 arrayList 저장
        if (getPokemons(name) == null) {
            ArrayList<Pokemon> arrayList = new ArrayList<>();
            pokemons.put(name, arrayList);
        }

        // 이미 있는 포켓몬이라면
        getPokemons(name).add(pokemon);
    }

    public Pokemon getStrongest(String name) {
        // name 이름의 포켓몬 목록
        ArrayList<Pokemon> pokemonList = getPokemons(name);

        // name 이름의 포켓몬 목록이 비어있으면 null을 리턴
        if (pokemonList == null) {
            return null;
        }

        // return할 포켓몬(가장 센 포켓몬)을 담을 변수
        Pokemon strongest = null;

        for (Pokemon pokemon : pokemonList) {
            if (strongest == null || pokemon.cp > strongest.cp) {
                strongest = pokemon;
            }
        }

        return strongest;
    }

    public Pokemon getStrongest() {
        Pokemon strongestPokemon = null;

        for (String name : pokemons.keySet()) {
            Pokemon strongPokemon = getStrongest(name);

            if (strongestPokemon == null || strongPokemon.cp > strongestPokemon.cp) {
                strongestPokemon = strongPokemon;
            }

        }
        return strongestPokemon;
    }
}
