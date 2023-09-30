use std::{
    collections::{HashSet, VecDeque},
    error::Error,
    io::stdin,
};

fn is_valid_cell(n: usize, visited: &HashSet<(isize, isize)>, cell: (isize, isize)) -> bool {
    cell.0 >= 0
        && cell.0 < n as isize
        && cell.1 >= 0
        && cell.1 < n as isize
        && !visited.contains(&cell)
}

const MOVE_DELTAS: [(isize, isize); 8] = [
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
];

fn main() -> Result<(), Box<dyn Error>> {
    let stdin = stdin();
    let mut buf = String::new();
    stdin.read_line(&mut buf)?;
    let n: usize = buf.trim_end().parse()?;
    let mut visited_cells = HashSet::<(isize, isize)>::new();
    let mut q = VecDeque::<(isize, isize, isize)>::new();
    for r in 0..n {
        buf.clear();
        stdin.read_line(&mut buf)?;
        for (c, s) in buf.chars().enumerate() {
            match s {
                '#' => {
                    visited_cells.insert((r as isize, c as isize));
                }
                'K' => {
                    q.push_back((r as isize, c as isize, 0));
                }
                _ => {}
            }
        }
    }
    loop {
        if let Some(knight) = q.pop_front() {
            if knight.0 == 0 && knight.1 == 0 {
                println!("{}", knight.2);
                break;
            }
            let new_positions: Vec<(isize, isize, isize)> = MOVE_DELTAS
                .iter()
                .map(|d| (d.0 + knight.0, d.1 + knight.1, knight.2 + 1))
                .filter(|pos| is_valid_cell(n, &visited_cells, (pos.0, pos.1)))
                .collect();
            for new_pos in new_positions {
                q.push_back(new_pos);
                visited_cells.insert((new_pos.0, new_pos.1));
            }
        } else {
            println!("-1");
            break;
        }
    }
    Ok(())
}
