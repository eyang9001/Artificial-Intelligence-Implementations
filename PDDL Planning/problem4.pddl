(define (problem soko-dai)
  (:domain sokorobotto)
  (:objects
    shipment1 shipment2 shipment3 shipment4 - shipment
    order1 order2 order3 order4 - order
    store1 store2 store3 store4 store5 store6 path1 path2 path3 path4 pack1 pack2 - location
    robot1 robot2 - robot
    pallette1 pallette2 pallette3 pallette4 pallette5 - pallette
    socks1 socks2 socks3 book1 book2 ball1 pillow1 tv1 computer1  - saleitem
    )
  (:init
    (ships shipment1 order1)
    (orders order1 socks1)
    (orders order1 book1)
    (unstarted shipment1)
    
    (ships shipment2 order2)
    (orders order2 socks2)
    (orders order2 pillow1)
    (unstarted shipment2)
    
    (ships shipment3 order3)
    (orders order3 tv1)
    (unstarted shipment3)
    
    (ships shipment4 order4)
    (orders order4 socks3)
    (orders order4 book2)
    (orders order4 ball1)
    (orders order4 computer1)
    (unstarted shipment4)
    
    (packing-location pack1)
    (available pack1)
    
    (packing-location pack2)
    (available pack2)
    
    (contains pallette1 socks1)
    (contains pallette1 socks2)
    (contains pallette1 socks3)
    (contains pallette1 pillow1)
    
    (contains pallette2 book1)
    (contains pallette2 book2)
    
    (contains pallette3 ball1)
    
    (contains pallette4 tv1)
    
    (contains pallette5 computer1)
    
    (free robot1)
    (free robot2)
    
    (connected store1 path1)
    (connected path1 store1)
    (connected store2 path1)
    (connected path1 store2)
    (connected path2 path1)
    (connected path1 path2)
    
    (connected store3 path2)
    (connected path2 store3)
    (connected store4 path2)
    (connected path2 store4)
    (connected path2 path3)
    (connected path3 path2)
    
    (connected store5 path3)
    (connected path3 store5)
    (connected store6 path3)
    (connected path3 store6)
    (connected path4 path3)
    (connected path3 path4)

    (connected pack1 path4)
    (connected path4 pack1)
    (connected pack2 path4)
    (connected path4 pack2)

    (at pallette1 store1)
    (at pallette2 store2)
    (at pallette3 store3)
    (at pallette4 store4)
    (at pallette5 store5)

    (at robot1 pack1)
    (at robot2 pack2)
    (no-robot store1)
    (no-robot store2)
    (no-robot store3)
    (no-robot store4)
    (no-robot store5)
    (no-robot store6)
    (no-robot path1)
    (no-robot path2)
    (no-robot path3)
    (no-robot path4)
    (no-pallette store6)
    (no-pallette pack1)
    (no-pallette pack2)
    (no-pallette path1)
    (no-pallette path2)
    (no-pallette path3)
    (no-pallette path4)
    )
  (:goal (and (includes shipment1 socks1)
              (includes shipment1 book1)
              (includes shipment2 socks2)
              (includes shipment2 pillow1)
              (includes shipment3 tv1)
              (includes shipment4 socks3)
              (includes shipment4 book2)
              (includes shipment4 ball1)
              (includes shipment4 computer1)))
)
