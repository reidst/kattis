use std::{error::Error, io::stdin};

fn main() -> Result<(), Box<dyn Error>> {
    let stdin = stdin();
    let mut pwa = String::new();
    let mut pwb = String::new();
    stdin.read_line(&mut pwa)?;
    stdin.read_line(&mut pwb)?;
    let count = pwa.chars().zip(pwb.chars()).filter(|(a, b)| a != b).count();
    println!("{}", 2usize.pow(count as u32));
    Ok(())
}
