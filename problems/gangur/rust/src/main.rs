// kattis-accepted
use std::{error::Error, io::stdin};

fn main() -> Result<(), Box<dyn Error>> {
    let stdin = stdin();
    let mut hall = String::new();
    stdin.read_line(&mut hall)?;
    let mut passes = 0usize;
    let mut rights = 0usize;
    for c in hall.chars() {
        match c {
            '>' => rights += 1,
            '<' => passes += rights,
            _ => {}
        }
    }
    println!("{passes}");
    Ok(())
}
