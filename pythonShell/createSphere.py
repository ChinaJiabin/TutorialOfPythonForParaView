from paraview.simple import *
from itertools import count
import string
########################################################################################
#Parameter

file_number=122;                                      
filepath='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.1\\MD\\one-dimensional\\vtk'
filename = ("particle_%05i.vtk" % i for i in count(1))
image_path='C:\\Users\\jiabin\\Documents\\MATLAB\\MD_project_2.1\\MD\\one-dimensional\\picture'
image_filename=("%05i.png" % i for i in count(1))

#########################################################################################
#View adjust

RenderView = GetRenderView();
RenderView.OrientationAxesVisibility = 0;
RenderView.CenterAxesVisibility = 0;

RenderView.CameraViewUp = [0.0, 1.0, 0.0]
RenderView.CameraFocalPoint = [-366.9905325328733, 1026.0664644773592, -3440.96229960942]
RenderView.CameraClippingRange = [262.94302774855396, 277.5371951159417]
RenderView.CameraPosition = [-366.9905325328733, 1026.0664644773592, 270.86669469550907]

#RenderView.CameraPosition = [91.0, 117.5, 576.0048862833432]
#RenderView.CameraFocalPoint = [91.0, 117.5, 1.75]

########################################################################################
#Create wall
wall=LegacyVTKReader( FileNames=[filepath+'\\wall.vtk'] )
wall_dp=GetActiveSource()
wall_dp=GetDisplayProperties(wall_dp)
wall_dp.Opacity=0.4;

########################################################################################
#Create spheres

while file_number:
     file_number=file_number-1;
     sphere=LegacyVTKReader( FileNames=[filepath+'\\'+next(filename)] )

     Show(wall)
     Show(sphere)
     sphere_dp = GetActiveSource()
     Glyph_sphere = Glyph( GlyphType="Sphere", GlyphTransform="Transform2" )
     Glyph_sphere.GlyphType.ThetaResolution = 50
     Glyph_sphere.GlyphType.PhiResolution = 50
     Glyph_sphere.GlyphType.Radius = 2
     Show(Glyph_sphere)
     Render()

     WriteImage(image_path+'\\'+next(image_filename))
     Delete(sphere)
     Delete( Glyph_sphere)
#########################################################################################