fn main() {
    let mut time = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut time).unwrap();
    let time = &time[0..4];

    let mut array = vec![
        vec![false, false, false, false],
        vec![false, false, false, false],
        vec![false, false, false, false],
        vec![false, false, false, false],
    ];

    for (i, digit) in time.chars().enumerate() {
        let digit = digit.to_digit(10).unwrap();
        for j in (0..4).rev() {
            array[3-j][i] = digit & 1<<j != 0;
        }
    }

    for row in array {
        let mapped = row.iter().map(|&b| 
            if b {"*"} else {"."}
        ).collect::<Vec<&str>>();
        println!("{} {}   {} {}",
            mapped[0],
            mapped[1],
            mapped[2],
            mapped[3]
        );
    }
}
