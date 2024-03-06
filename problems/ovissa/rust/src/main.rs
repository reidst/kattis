fn main() -> std::result::Result<(), Box<dyn std::error::Error>> {
    let stdin = std::io::stdin();
    let mut u = String::with_capacity(10_000);
    stdin.read_line(&mut u).unwrap();
    println!("{}", u.trim_end().chars().count());
    Ok(())
}
