// kattis-accepted
fn main() {
    let mut line = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut line).unwrap();
    let sum = line.split_whitespace()
        .map( |x| 
            x.parse::<usize>().unwrap()
        ).sum::<usize>();
    println!("{}", sum);
}
