(define (problem soko-ni-pallette)
  (:domain sokorobotto)
  (:objects
    shipment1 - shipment
    order1 - order
    loc1 loc2 pack1 - location
    robot1 robot2 - robot
    pallette1 pallette2 - pallette
    ball1 socks1 book1 book2 - saleitem
    )
  (:init
    (ships shipment1 order1)
    (orders order1 ball1)
    (orders order1 book2)
    (unstarted shipment1)
    (contains pallette2 ball1)
    (contains pallette2 book2)
    (contains pallette1 socks1)
    (contains pallette1 book1)
    (packing-location pack1)
    (available pack1)
    (free robot1)
    (free robot2)
    (connected loc1 loc2)
    (connected loc2 loc1)
    (connected loc2 pack1)
    (connected pack1 loc2)
    (at pallette1 loc1)
    (at pallette2 loc2)
    (at robot1 loc2)
    (at robot2 pack1)
    (no-robot loc1)
    (no-pallette pack1)
    (available pack1)
    )
  (:goal (and (includes shipment1 ball1)
              (includes shipment1 book2)))
)