<?php

use Symfony\Component\HttpFoundation\Request;
use Symfony\Component\HttpFoundation\Response;

use GuideApp\Entity\Step as StepEntity;

require_once '../bootstrap.php';

$app->get('/scenario/subpage/steps', function (Request $request) use ($app) {
   
   
    $steps = $app['entityManager']->getRepository('GuideApp:Repository:Step')->findBy([
        'scenario_hash' => $request->get('scenario_hash'),
        'subpage_path' => $request->get('subpage_path')
    ]); 
   
   return new Response(json_encode($steps), 200);;
});

$app->run();