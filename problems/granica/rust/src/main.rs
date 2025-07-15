// kattis-accepted
use std::io::stdin;

fn isqrt(x: usize) -> usize {
    return isqrt_up(x, 1);
}

fn isqrt_up(x: usize, i: usize) -> usize {
    if x == 0 { return 0; }
    if i * i <= x {
        return isqrt_up(x, 2 * i);
    } else {
        return isqrt_down(x, i / 2, i);
    }
}

fn isqrt_down(x: usize, l: usize, h: usize) -> usize {
    if h - l < 2 { return l; }
    let m = (h - l) / 2 + l;
    if m * m <= x {
        return isqrt_down(x, m, h);
    } else {
        return isqrt_down(x, l, m);
    }
}

fn gcd(a: usize, b: usize) -> usize {
    if usize::min(a, b) == 0 {
        usize::max(a, b)
    } else {
        gcd(b, a % b)
    }
}

fn smallest_factor(x: usize) -> usize {
    for i in 2..=isqrt(x) {
        if x % i == 0 { return i; }
    }
    x
}

fn prime_factors(x: usize) -> Vec<(usize, usize)> {
    if x == 1 { return Vec::new() }
    let sf = smallest_factor(x);
    let mut k = x;
    let mut c = 0usize;
    while k % sf == 0 {
        k = k / sf;
        c = c + 1;
    }
    let mut rest = prime_factors(k);
    rest.push((sf, c));
    rest
}

fn powermultiset(mut s: Vec<(usize, usize)>) -> Vec<Vec<usize>> {
    match s.pop() {
        None => vec![vec![]],
        Some((h, c)) => {
            let tp = powermultiset(s);
            let mut p = vec![];
            for sub in tp {
                let mut mut_sub = sub.clone();
                p.push(mut_sub.clone());
                for _ in 0..c {
                    mut_sub.push(h);
                    p.push(mut_sub.clone());
                }
            }
            p
        }
    }
}

fn mapprod(l: Vec<Vec<usize>>) -> Vec<usize> {
    l.iter().map(|s| s.into_iter().fold(1, |a, x| a * x)).collect()
}

fn divisors(x: usize) -> Vec<usize> {
    mapprod(powermultiset(prime_factors(x)))
}

fn read_usize() -> usize {
    let mut s = String::new();
    stdin().read_line(&mut s).expect("failed to read line");
    s.trim().parse().expect("failed to parse usize")
}

fn get_input() -> Vec<usize> {
    // first num, 2 <= N <= 100
    let n = read_usize();
    // following N nums, 1 <= x <= 10^9
    let mut nums = Vec::with_capacity(n);
    for _ in 0..n {
        nums.push(read_usize());
    }
    nums
}

fn main() {
    let nums = get_input();
    let mut g = 0;
    for i in 0..nums.len() {
        for j in i+1..nums.len() {
            let diff = {
                let a = nums[i];
                let b = nums[j];
                if a > b { a - b } else { b - a }
            };
            g = gcd(g, diff);
        }
    }
    for d in divisors(g) {
        if d > 1 {
            print!("{d} ");
        }
    }
}
