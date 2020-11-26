use console::style;
use log::warn;
use std::io;
// mod sub_sequece;
// mod generate_all_combinations;
// mod hamitonian_cycle;
// mod sub_sequece;
mod coloring;

macro_rules! success {
    ($fmt:literal, $ex:expr) => {{
        use console::{style, Emoji};
        let formatstr = format!($fmt, $ex);
        println!(
            "{} {}",
            style(Emoji("✅", "✓")).white(),
            style(formatstr).red()
        );
    }};
}

fn main() {
    // all_permutations::all_permutations(3, 2);
    // let v: Vec<i32> = vec![1, 2, 3];
    // sub_sequece::sub_sequence(v);
    // sub_sequece::sub_sequence_main();
    // hamitonian_cycle::hamitonian_cycle_test)(
    // coloring::coloring_test()
    let mut a = String::new();
    io::stdin().read_line(&mut a).expect("failed to read line");
    success!("hello done {}", a);
}
